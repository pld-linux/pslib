Summary:	The pslib C-library to create PostScript on the fly
Summary(pl.UTF-8):	Biblioteka do generowania w locie plików PostScript
Name:		pslib
Version:	0.4.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pslib/%{name}-%{version}.tar.gz
# Source0-md5:	64ca84f1832f1d01e163c510c28bc6a9
URL:		http://pslib.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	docbook-to-man
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel >= 5
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pslib is a C-library to create PostScript files on the fly. It offers
many drawing primitives, inclusion of PNG and EPS images and a very
sophisticated text rendering including hyphenation, kerning and
ligatures. It can read external Type1 fonts and embed them into the
output file. It supports pdfmarks which makes it in combination with
ghostscript's pdfwriter an alternative for libraries creating PDF.

%description -l pl.UTF-8
pslib to biblioteka C do tworzenia w locie plików PostScript. Oferuje
rysowanie wielu prymitywów, włączanie obrazów PNG i EPS oraz bardzo
wyszukane renderowanie tekstu włącznie z przenoszeniem, kerningiem i
ligaturami. Może wczytywać zewnętrzne fonty Type1 i osadzać je w pliku
wyjściowym. Obsługuje pdfmarki, co, w połączeniu z pdfwriterem z
ghostscripta, czyni ją alternatywą dla bibliotek tworzących PDF.

%package devel
Summary:	Development files for the pslib C-library to create PostScript
Summary(pl.UTF-8):	Pliki programistyczne dla biblioteki C pslib tworzącej PostScript
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the pslib C-library to create PostScript files
on the fly.

%description devel -l pl.UTF-8
Pliki programistyczne dla biblioteki C pslib tworzącej w locie pliki
PostScript.

%package static
Summary:	Static pslib library
Summary(pl.UTF-8):	Statyczna biblioteka pslib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static pslib library.

%description static -l pl.UTF-8
Statyczna biblioteka pslib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libps.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libps.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libps.so
%{_includedir}/libps
%{_pkgconfigdir}/libps.pc
%{_mandir}/man3/pslib.3*
%{_mandir}/man3/PS_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libps.a

Summary:	The pslib C-library to create PostScript on the fly
Summary(pl.UTF-8):	Biblioteka do generowania w locie plików PostScript
Name:		pslib
Version:	0.4.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/pslib/%{name}-%{version}.tar.gz
# Source0-md5:	78693d87d89fe7fcc7bc45e54b7b64a6
Patch0:		%{name}-getline.patch
URL:		http://pslib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-to-man
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

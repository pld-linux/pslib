Summary:	The pslib C-library to create PostScript on the fly
Summary(pl):	Biblioteka do generowania w locie plików PostScript
Name:		pslib
Version:	0.2.5
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/pslib/%{name}-%{version}.tar.gz
# Source0-md5:	12cf52461658fe32524975896771b66d
URL:		http://pslib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pslib is a C-library to create PostScript files on the fly. It offers
many drawing primitives, inclusion of PNG and EPS images and a very
sophisticated text rendering including hyphenation, kerning and
ligatures. It can read external Type1 fonts and embed them into the
output file. It supports pdfmarks which makes it in combination with
ghostscript's pdfwriter an alternative for libraries creating PDF.

%description -l pl
pslib to biblioteka C do tworzenia w locie plików PostScript. Oferuje
rysowanie wielu prymitywów, w³±czanie obrazów PNG i EPS oraz bardzo
wyszukane renderowanie tekstu w³±cznie z przenoszeniem, kerningiem i
ligaturami. Mo¿e wczytywaæ zewnêtrzne fonty Type1 i osadzaæ je w pliku
wyj¶ciowym. Obs³uguje pdfmarki, co, w po³±czeniu z pdfwriterem z
ghostscripta, czyni j± alternatyw± dla bibliotek tworz±cych PDF.

%package devel
Summary:	Development files for the pslib C-library to create PostScript
Summary(pl):	Pliki programistyczne dla biblioteki C pslib tworz±cej PostScript
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the pslib C-library to create PostScript files
on the fly.

%description devel -l pl
Pliki programistyczne dla biblioteki C pslib tworz±cej w locie pliki
PostScript.

%package static
Summary:	Static pslib library
Summary(pl):	Statyczna biblioteka pslib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static pslib library.

%description static -l pl
Statyczna biblioteka pslib.

%prep
%setup -q

%build
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

Summary:	The pslib C-library to create PostScript on the fly
Summary(pl):	Biblioteka do generowania w locie plików PostScript
Name:		pslib
Version:	0.2.5
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/pslib/%{name}-%{version}.tar.gz
# Source0-md5:	12cf52461658fe32524975896771b66d
URL:		http://pslib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pslib is a C-library to create PostScript files on the fly. It offers
many drawing primitives, inclusion of png and eps images and a very
sophisticated text rendering including hyphenation, kerning and
ligatures. It can read external Type1 fonts and embed them into the
output file. It supports pdfmarks which makes it in combination with
ghostscript's pdfwriter an alternative for libraries creating PDF.

%package devel
Summary:	Development files for the pslib C-library to create PostScript
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the pslib C-library to create PostScript files
on the fly. It offers many drawing primitives, inclusion of png and
eps images and a very sophisticated text rendering including
hyphenation, kerning and ligatures. It can read external Type1 fonts
and embed them into the output file. It supports pdfmarks which makes
it in combination with ghostscript's pdfwriter an alternative for
libraries creating PDF.

%package static
Summary:	Static libraries for the pslib C-library to create PostScript
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libraries for the pslib C-library to create PostScript files on
the fly. It offers many drawing primitives, inclusion of png and eps
images and a very sophisticated text rendering including hyphenation,
kerning and ligatures. It can read external Type1 fonts and embed them
into the output file. It supports pdfmarks which makes it in
combination with ghostscript's pdfwriteran alternative for libraries
creating PDF.


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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*
#{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

Name: odt2txt
Version: 0.4
Release: alt1
Summary: Extract text from OpenDocument Text files
License: %gpl2only
Group: Text tools
URL: http://stosberg.net/%name
Source: %url/%name-%version.tar

# Automatically added by buildreq on Tue Nov 06 2007
BuildRequires: zlib-devel
BuildRequires: rpm-build-licenses

%description
%name extracts the text out of OpenDocument Texts. It is small, fast
and portable, can output the document in your console encoding, and has
very few external dependencies.


%prep
%setup


%build
%make_build CFLAGS="%optflags"


%install
%if 1
%make_install DESTDIR=%buildroot PREFIX=%_prefix install
%else
install -D -m 0755 {,%buildroot%_bindir/}%name
install -D -m 0644 {,%buildroot%_man1dir/}%name.1
%endif


%files
%_bindir/*
%_man1dir/*


%changelog
* Wed Aug 20 2008 Led <led@altlinux.ru> 0.4-alt1
- 0.4

* Tue Nov 06 2007 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- build for Sisyphus (spec from Dag Wieers repos)

* Mon Jun 25 2007 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.

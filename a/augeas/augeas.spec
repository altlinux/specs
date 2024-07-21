Name: augeas
Version: 1.14.1
Release: alt1
Summary: A library for changing configuration files

Group: System/Configuration/Other
License: LGPLv2+
Url: http://augeas.net/
Vcs: https://github.com/hercules-team/augeas
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: readline-devel libselinux-devel gnulib flex perl-podlators ruby-stdlibs libxml2-devel
# for tests
BuildRequires: /proc
Requires: vim-common

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
The libraries for %name.

%prep
%setup -q
%patch -p1

%build
./autogen.sh --gnulib-srcdir=/usr/share/gnulib
%configure --disable-static --disable-gnulib-tests
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/*
%_mandir/man1/*
%_datadir/bash-completion/completions/*
%_datadir/vim/vimfiles/syntax/augeas.vim
%_datadir/vim/vimfiles/ftdetect/augeas.vim

%files -n lib%name
%_datadir/augeas
%_libdir/*.so.*
%doc AUTHORS COPYING NEWS

%files -n lib%name-devel
%doc
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/augeas.pc

%changelog
* Tue Jul 16 2024 Anton Farygin <rider@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 1.13.0-alt1
- 1.13.0

* Thu Apr 18 2019 Anton Farygin <rider@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Wed Feb 06 2019 Anton Farygin <rider@altlinux.ru> 1.11.0-alt2
- rebuilt with recent gnulib

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Sun Apr 01 2018 Anton Farygin <rider@altlinux.ru> 1.10.1-alt1
- new version

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- new version

* Sun Jun 21 2015 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- new version

* Fri Nov 21 2014 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- new version

* Thu Feb 20 2014 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version

* Wed Jul 31 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0-alt1
- New version

* Sun Mar 17 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version (closes: #28696)
- Fix CVE-2012-0786, CVE-2012-0787
- Apply patch for fix test-run https://fedorahosted.org/augeas/ticket/332

* Thu Dec 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.10.0-alt1
- New version

* Thu Sep 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.0-alt1
- New version

* Wed Jul 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.1-alt1
- New version

* Fri Feb 25 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.0-alt1
- New version
- Fix bootstrap for make shared lib gnulib
- Use system gnulib
- Enable tests and fix it
- Build with libselinux support

* Thu Dec 02 2010 Anton Farygin <rider@altlinux.ru> 0.7.4-alt1
- new version

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Oct 01 2010 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- new version

* Mon Nov 09 2009 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- first build for Sisyphus

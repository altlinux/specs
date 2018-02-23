%define pkgname ffi

Name: ruby-%pkgname
Version: 1.9.22
Release: alt1

Summary: Ruby foreign function interface
Group: Development/Ruby
License: BSD
Url: https://github.com/ffi/ffi

Source: %pkgname-%version.tar
Patch1: %name-alt-fix-requires.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel libruby-devel ruby-tool-setup

%filter_from_requires \,^ruby(lib/ffi/.*generator),d

%description
A Ruby foreign function interface.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch1 -p1
%update_setup_rb

sed -i -r '/^[[:blank:]]*Data_Get_Struct\(/s/^(([[:blank:]]*).*)((field) = layout->fields\[i\])(\).*)$/\2\3;\n\1\4\5/' \
	ext/ffi_c/StructLayout.c

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README.md LICENSE
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.22-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.21-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Mar 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt1
- New version

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.17-alt1
- new version 1.9.17
- fix module requires pathes

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.14-alt1
- new version 1.9.14

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version
- Fix project URL

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.6.3-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.6.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus


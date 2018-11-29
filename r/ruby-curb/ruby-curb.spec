%define  pkgname curb

Name: 	 ruby-%pkgname
Version: 0.9.7
Release: alt1

Summary: Ruby bindings for libcurl
License: MIT/ruby
Group:   Development/Ruby
Url:     https://github.com/taf2/curb

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libcurl-devel

%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for
the libcurl(3), a fully-featured client-side URL transfer library. cURL and
libcurl live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config -- --use-system-libraries
%ruby_build

%install
%ruby_install
%rdoc lib/
find %buildroot
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Nov 07 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.7-alt1
- Bump to 0.9.7

* Fri Nov 02 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.6-alt1
- Bump to 0.9.6.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.6
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.5
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Leonid Krivoshein <klark@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

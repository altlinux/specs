%define        pkgname curb

Name: 	       ruby-%pkgname
Version:       0.9.9
Release:       alt1
Summary:       Ruby bindings for libcurl
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/taf2/curb
# VCS:         https://github.com/taf2/curb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         version.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcurl-devel

%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for
the libcurl(3), a fully-featured client-side URL transfer library. cURL and
libcurl live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup
%patch -p1

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.9-alt1
- Bump to 0.9.9
- Use Ruby Policy 2.0

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

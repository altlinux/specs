%define        pkgname yard

Name:          ruby-%pkgname
Version:       0.9.19
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!"
License:       MIT
Group:         Development/Ruby
Url:           https://yardoc.org/
# VCS:         https://github.com/lsegal/yard.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem


%package       -n yard
Summary:       Yard, Yardoc, and Yri executables for yard gem
Group:         Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.19-alt1
- Bump to 0.9.19
- Use Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus, packaged as a gem

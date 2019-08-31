# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname safe_yaml

Name:          ruby-%pkgname
Version:       1.0.5
Release:       alt1
Summary:       Parse YAML safely
Group:         Development/Ruby
License:       MIT
URL: 	       https://github.com/dtao/safe_yaml
%vcs           https://github.com/dtao/safe_yaml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
Source:        %name-%version.tar

%description
The SafeYAML gem provides an alternative implementation of
YAML.load suitable for accepting user input in Ruby applications.
Unlike Ruby's built-in implementation of YAML.load, SafeYAML's
version will not expose apps to arbitrary code execution exploits.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- Bump to 1.0.5
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux

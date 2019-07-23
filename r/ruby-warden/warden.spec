# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname warden

Name:          ruby-%pkgname
Version:       1.2.8
Release:       alt1
Summary:       General Rack Authentication Framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/wardencommunity/warden
%vcs           https://github.com/wardencommunity/warden.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.


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

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- Bump to 1.2.8
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.4-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 02 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt2
- added README.alt

* Wed Feb 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

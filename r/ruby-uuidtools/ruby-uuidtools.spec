# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname uuidtools

Name:          ruby-%pkgname
Version:       2.1.5
Release:       alt2
Summary:       A simple universally unique ID generation library
Group:         Development/Ruby
License:       MIT
Url:           http://github.com/sporkmonger/uuidtools
%vcs           http://github.com/sporkmonger/uuidtools.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
UUIDTools was designed to be a simple library for generating any
of the various types of UUIDs.  It conforms to RFC 4122 whenever
possible.


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
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.5-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1
- New version
- Disable use deprecated thread module

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- Built for Sisyphus


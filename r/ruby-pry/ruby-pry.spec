%define        pkgname pry

Name: 	       ruby-%pkgname
Version:       0.12.2
Release:       alt3
Summary:       An IRB alternative and runtime developer console
License:       MIT
Group:         Development/Ruby
Url:           http://pryrepl.org/
%vcs           https://github.com/pry/pry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(yard) 
BuildRequires: gem(rspec) >= 3.8.0
BuildRequires: gem(rspec-expectations) = 3.8.2
BuildRequires: gem(simplecov) >= 0.16
BuildRequires: gem(rubocop) >= 0.74

%description
Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
from scratch to provide a number of advanced features.


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
%ruby_build --ignore=fixtures

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%_bindir/%pkgname
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 02 2019 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt3
! spec, build depedencies

* Tue Jul 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt2
- Use Ruby Policy 2.0

* Thu Nov 15 2018 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt1
- Bump to 0.12.2.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Mar 09 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.3-alt1
- new version 0.11.3

* Sun Sep 10 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.4-alt3.2
- Rebuild with Ruby 2.4.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.4-alt3.1
- Rebuild with Ruby 2.4.1

* Mon May 29 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt3
- Remove doc package because exists pry-doc -- documentation plugin for pry

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt2
- Add requires to ruby-slop3

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.10.4-alt1
- Initial build in Sisyphus

%define        gemname pry

Name:          gem-pry
Version:       0.14.1
Release:       alt1
Summary:       An IRB alternative and runtime developer console
License:       MIT
Group:         Development/Ruby
Url:           http://pryrepl.org/
Vcs:           https://github.com/pry/pry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(coderay) >= 1.1 gem(coderay) < 2
BuildRequires: gem(method_source) >= 1.0 gem(method_source) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names fixtures
Requires:      gem(coderay) >= 1.1 gem(coderay) < 2
Requires:      gem(method_source) >= 1.0 gem(method_source) < 2
Obsoletes:     ruby-pry < %EVR
Provides:      ruby-pry = %EVR
Provides:      gem(pry) = 0.14.1


%description
Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
from scratch to provide a number of advanced features.


%package       -n pry
Version:       0.14.1
Release:       alt1
Summary:       An IRB alternative and runtime developer console executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета pry
Group:         Other
BuildArch:     noarch

Requires:      gem(pry) = 0.14.1

%description   -n pry
An IRB alternative and runtime developer console executable(s).

Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
from scratch to provide a number of advanced features.

%description   -n pry -l ru_RU.UTF-8
Исполнямка для самоцвета pry.


#%package       -n gem-pry-doc
#Version:       0.14.1
#Release:       alt1
#Summary:       An IRB alternative and runtime developer console documentation files
#Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry
#Group:         Development/Documentation
#BuildArch:     noarch
#
#Requires:      gem(pry) = 0.14.1
#
#%description   -n gem-pry-doc
#An IRB alternative and runtime developer console documentation files.
#
#Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
#from scratch to provide a number of advanced features.
#
#%description   -n gem-pry-doc -l ru_RU.UTF-8
#Файлы сведений для самоцвета pry.
#
#
%package       -n gem-pry-devel
Version:       0.14.1
Release:       alt1
Summary:       An IRB alternative and runtime developer console development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry) = 0.14.1

%description   -n gem-pry-devel
An IRB alternative and runtime developer console development package.

Pry is a powerful alternative to the standard IRB shell for Ruby. It is written
from scratch to provide a number of advanced features.

%description   -n gem-pry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n pry
%doc README.md
%_bindir/pry

#%files         -n gem-pry-doc
#%doc README.md
#%ruby_gemdocdir
#
%files         -n gem-pry-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 0.14.1-alt1
- ^ 0.13.1 -> 0.14.1

* Thu Apr 23 2020 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- ^ 0.12.2 -> 0.13.1

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt3.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt3.1
- fixed (!) spec according to changelog rules

* Mon Sep 02 2019 Pavel Skrylev <majioa@altlinux.org> 0.12.2-alt3
- fixed (!) spec, build depedencies

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

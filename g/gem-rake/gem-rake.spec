%define        _unpackaged_files_terminate_build 1
%define        gemname rake

Name:          gem-rake
Version:       13.1.0
Release:       alt1
Summary:       Ruby based make-like utility
License:       MIT
Group:         Development/Ruby
Url:           https://ruby.github.io/rake/
Vcs:           https://github.com/ruby/rake.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rake) = 13.1.0

%ruby_bindir_to %ruby_bindir

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%description         -l ru_RU.UTF-8
Rake есть Make-подобная утилита и набор модулей, исполненные на рубине. Задачи и
зависимости описываются в рядовом правописании рубина.


%package       -n rake
Version:       13.1.0
Release:       alt1
Summary:       Ruby based make-like utility executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake) = 13.1.0

%description   -n rake
Ruby based make-like utility executable(s).

Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%description   -n rake -l ru_RU.UTF-8
Исполнямка для самоцвета rake.


%package       -n gem-rake-doc
Version:       13.1.0
Release:       alt1
Summary:       Ruby based make-like utility documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rake) = 13.1.0

%description   -n gem-rake-doc
Ruby based make-like utility documentation files.

Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%description   -n gem-rake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rake.


%package       -n gem-rake-devel
Version:       13.1.0
Release:       alt1
Summary:       Ruby based make-like utility development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake) = 13.1.0
Requires:      gem(minitest) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-rake-devel
Ruby based make-like utility development package.

Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%description   -n gem-rake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rake.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n rake
%doc README.rdoc
%ruby_bindir/rake
%ruby_mandir/rake.1.xz

%files         -n gem-rake-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-rake-devel
%doc README.rdoc


%changelog
* Thu Nov 30 2023 Pavel Skrylev <majioa@altlinux.org> 13.1.0-alt1
- ^ 13.0.6 -> 13.1.0

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 13.0.6-alt1
- ^ 13.0.5 -> 13.0.6

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 13.0.5-alt1
- ^ 13.0.1 -> 13.0.5

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 13.0.1-alt0.1
- ^ 12.3.3 -> 13.0.1
- ! spec tags

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.3-alt1
- update (^) 12.3.2 -> 12.3.3
- fix (!) spec to allow building

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt3
- Use Ruby Policy 2.0

* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt2
- Fix the executable, which is being get from proper source;
- Place library files into gem folder.

* Fri Dec 28 2018 Pavel Skrylev <majioa@altlinux.org> 12.3.2-alt1
- Bump to 12.3.2.
- Russian descriptions.

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.8.7-alt3
- Rebuild with new ruby.

* Tue Jan 04 2011 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Updated to rake-0.8.7-134-g9dad179

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt1
- [0.8.7]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.4-alt1
- [0.8.4]

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 0.8.1-alt1
- [0.8.1]

* Thu Jan 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt2
- Add ruby-module-misc to requires

* Tue May 22 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Thu Jul 06 2006 Sir Raorn <raorn@altlinux.ru> 0.7.1-alt1
- [0.7.1]

* Tue Mar 07 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt2
- header in /usr/bin/rake fixed [#9195]

* Thu Feb 16 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Aug 31 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.5.4-alt1
- Initial build for ALT Linux

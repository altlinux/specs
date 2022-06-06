%define        gemname jaro_winkler

Name:          gem-jaro-winkler
Version:       1.5.4.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string
Summary(ru_RU.UTF-8): Воплощение алгоритма расстояний Яро-Винклера на Си и Рубине, который поддерживает строки UTF-8
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tonytonyjan/jaro_winkler
Vcs:           https://github.com/tonytonyjan/jaro_winkler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.7 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_alias_names jaro_winkler,jaro-winkler
Provides:      gem(jaro_winkler) = 1.5.4.1

%ruby_use_gem_version jaro_winkler:1.5.4.1

%description
jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.


%package       -n gem-jaro-winkler-doc
Version:       1.5.4.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jaro_winkler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jaro_winkler) = 1.5.4.1

%description   -n gem-jaro-winkler-doc
Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8
string documentation files.

jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.

%description   -n gem-jaro-winkler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jaro_winkler.


%package       -n gem-jaro-winkler-devel
Version:       1.5.4.1
Release:       alt1
Summary:       Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jaro_winkler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jaro_winkler) = 1.5.4.1
Requires:      gem(bundler) >= 1.7 gem(bundler) < 3
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(rake-compiler) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-jaro-winkler-devel
Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8
string development package.

jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms other
than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation support
any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.

%description   -n gem-jaro-winkler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jaro_winkler.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-jaro-winkler-doc
%ruby_gemdocdir

%files         -n gem-jaro-winkler-devel
%ruby_includedir/*


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.4.1-alt1
- ^ 1.5.4 -> 1.5.4.1

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- ^ 1.5.3 -> 1.5.4
- ! spec tags

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1.1
- ! spec according to changelog rules

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.3-alt1
- ^ v1.5.3
- ! spec

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- remove noarch from devel package
- cleanup spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

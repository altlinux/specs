%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%def_enable    java
%define        gemname nokogiri

Name:          gem-nokogiri
Version:       1.16.4
Release:       alt1
Summary:       Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser)
License:       MIT
Group:         Development/Ruby
Url:           https://nokogiri.org/
Vcs:           https://github.com/sparklemotion/nokogiri.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         shutdown-libxml2-warning.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: zlib-devel
BuildRequires: gem(mini_portile2) >= 2.8.2
BuildConflicts: gem(mini_portile2) >= 2.9
%if_enabled check
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(rexical) = 1.0.7
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-parallel_fork) = 2.0.0
BuildRequires: gem(ruby_memcheck) >= 2.2.1
BuildRequires: gem(rubyzip) >= 2.3.2
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-shopify) >= 2.14.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(racc) >= 1.4
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ruby_memcheck) >= 3
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-shopify) >= 3
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(racc) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-shopify >= 2.14.0,rubocop-shopify < 3
%ruby_use_gem_dependency ruby_memcheck >= 2.2.1,ruby_memcheck < 3
%ruby_use_gem_dependency rubyzip >= 2.3.2,rubyzip < 3
Requires:      gem(mini_portile2) >= 2.8.2
Requires:      gem(racc) >= 1.4
Conflicts:     gem(mini_portile2) >= 2.9
Conflicts:     gem(racc) >= 2
Obsoletes:     ruby-nokogiri < %EVR
Provides:      ruby-nokogiri = %EVR
Provides:      gem(nokogiri) = 1.16.4


%description
Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support. This package
contanis Ruby libraries for Nokogiri.


%package       -n nokogiri
Version:       1.16.4
Release:       alt1
Summary:       Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета nokogiri
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(nokogiri) = 1.16.4

%description   -n nokogiri
Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser)
executable(s).

Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support. This package
contanis Ruby libraries for Nokogiri.

%description   -n nokogiri -l ru_RU.UTF-8
Исполнямка для самоцвета nokogiri.


%if_enabled    doc
%package       -n gem-nokogiri-doc
Version:       1.16.4
Release:       alt1
Summary:       Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nokogiri
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(nokogiri) = 1.16.4

%description   -n gem-nokogiri-doc
Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser) documentation
files.

Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support. This package
contanis Ruby libraries for Nokogiri.

%description   -n gem-nokogiri-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nokogiri.
%endif

%if_enabled    devel
%package       -n gem-nokogiri-devel
Version:       1.16.4
Release:       alt1
Summary:       Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nokogiri
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(nokogiri) = 1.16.4
Requires:      gem(mutex_m) >= 0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(rexical) = 1.0.7
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(minitest-parallel_fork) = 2.0.0
Requires:      gem(ruby_memcheck) >= 2.2.1
Requires:      gem(rubyzip) >= 2.3.2
Requires:      gem(simplecov) >= 0.17
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-shopify) >= 2.14.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      libxml2-devel
Requires:      libxslt-devel
%if_enabled java
Requires:      java-devel
%endif
Requires:      zlib-devel
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ruby_memcheck) >= 3
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-shopify) >= 3
Conflicts:     gem(rdoc) >= 7

%description   -n gem-nokogiri-devel
Ruby libraries for Nokogiri (HTML, XML, SAX, and Reader parser) development
package.

Nokogiri parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support. This package
contanis Ruby libraries for Nokogiri.

%description   -n gem-nokogiri-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nokogiri.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE-DEPENDENCIES.md LICENSE.md README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n nokogiri
%doc LICENSE-DEPENDENCIES.md LICENSE.md README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%_bindir/nokogiri

%if_enabled    doc
%files         -n gem-nokogiri-doc
%doc LICENSE-DEPENDENCIES.md LICENSE.md README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-nokogiri-devel
%doc LICENSE-DEPENDENCIES.md LICENSE.md README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_includedir/*
%endif


%changelog
* Sun Apr 21 2024 Pavel Skrylev <majioa@altlinux.org> 1.16.4-alt1
- ^ 1.16.2 -> 1.16.4
- ! protected java with if clause (closes #47259)

* Fri Feb 09 2024 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt1
- ^ 1.15.5 -> 1.16.2
- ! fixed CVE-2024-25062

* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.15.5-alt1
- ^ 1.13.8 -> 1.15.5

* Thu Oct 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.8-alt1.1
- !build requires gemlist closing it under the with check condition

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.8-alt1
- ^ 1.13.6 -> 1.13.8

* Fri Jun 10 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.6-alt1
- ^ 1.13.4 -> 1.13.6

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.4-alt1
- ^ 1.13.2 -> 1.13.4
- !address CVE-2022-24836
- !address CVE-2018-25032
- !address CVE-2022-23437
- !address CVE-2022-24839

* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.2-alt1
- ^ 1.13.1 -> 1.13.2

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.1-alt1
- ^ 1.12.5 -> 1.13.1

* Mon Dec 06 2021 Pavel Skrylev <majioa@altlinux.org> 1.12.5-alt1
- ^ 1.12.4 -> 1.12.5
- ! CVE-2021-41098

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.12.4-alt1
- ^ 1.11.1 -> 1.12.4
- ! fixes
 + CVE-2019-20388
 + CVE-2020-24977
 + CVE-2021-3517
 + CVE-2021-3518
 + CVE-2021-3537
 + CVE-2021-3541

* Fri Jan 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1
- ^ 1.11.0rc2+ -> 1.11.1
- ! spec

* Tue Jun 09 2020 Pavel Skrylev <majioa@altlinux.org> 1.11.0-alt0.2
- ^ 1.11.0rc1 -> 1.11.0rc2+

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 1.11.0-alt0.1
- ^ 1.10.7 -> 1.11.0rc1
- ! spec tags and syntax, requires for the devel package

* Mon Dec 09 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.7-alt1
- updated (^) 1.10.4 -> 1.10.7
- added (+) requires for devel package

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.4-alt1
- updated (^) 1.10.3 -> 1.10.4

* Tue Jun 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.3-alt2
- Fix spec

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.10.3-alt1
- New version.

* Mon Feb 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt4
- Use Ruby Policy 2.0.

* Fri Jan 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt3
- Fixed extension installation folder.

* Fri Jan 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt2
- Fixed spec.

* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- Bump to 1.10.1;
- Place library files into gem folder.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.5-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1
- New version.
- Package as gem.
- Simplify requirements and add requirements for rake tasks.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.3-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Nrw version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.0.1-alt1
- New version
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.6.2-alt1
- 1.6.6.2
- Rebuild with new version of libxml2

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.6.1-alt2
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 12 2013 Led <led@altlinux.ru> 1.5.9-alt1
- 1.5.9
- updated URL
- updated BuildRequires
- fixed Group for gem-nokogiri-doc subpackage
- moved %%_bindir/nokogiri to separate subpackage

* Sat Dec 15 2012 Led <led@altlinux.ru> 1.5.5-alt2
- fixed for renamed %%_bindir/rex -> %%_bindir/rexical

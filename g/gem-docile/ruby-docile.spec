%define        gemname docile

Name:          gem-docile
Version:       1.3.5
Release:       alt1
Summary:       Docile keeps your Ruby DSLs tame and well-behaved
License:       MIT
Group:         Development/Ruby
Url:           https://ms-ati.github.io/docile/
Vcs:           https://github.com/ms-ati/docile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 0
%ruby_ignore_names rspec_rails,faked_project,monorepo,parallel_tests,base,extra
Obsoletes:     ruby-docile < %EVR
Provides:      ruby-docile = %EVR
Provides:      gem(docile) = 1.3.5

%description
Docile is a small, self-contained Ruby library, that let's you map a DSL (domain
specific language) to your Ruby objects in a snap.


%package       -n gem-docile-doc
Version:       1.3.5
Release:       alt1
Summary:       Docile keeps your Ruby DSLs tame and well-behaved. documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета docile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(docile) = 1.3.5

%description   -n gem-docile-doc
Docile keeps your Ruby DSLs tame and well-behaved. documentation files.

Docile treats the methods of a given ruby object as a DSL (domain specific
language) within a given block.

Killer feature: you can also reference methods, instance variables, and local
variables from the original (non-DSL) context within the block.

Docile releases follow Semantic Versioning as defined at semver.org.

%description   -n gem-docile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета docile.


%package       -n gem-docile-devel
Version:       1.3.5
Release:       alt1
Summary:       Docile keeps your Ruby DSLs tame and well-behaved. development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета docile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(docile) = 1.3.5
Requires:      gem(rake) >= 0

%description   -n gem-docile-devel
Docile keeps your Ruby DSLs tame and well-behaved. development package.

Docile treats the methods of a given ruby object as a DSL (domain specific
language) within a given block.

Killer feature: you can also reference methods, instance variables, and local
variables from the original (non-DSL) context within the block.

Docile releases follow Semantic Versioning as defined at semver.org.

%description   -n gem-docile-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета docile.


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

%files         -n gem-docile-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-docile-devel
%doc README.md


%changelog
* Wed Apr 28 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- ^ 1.3.1 -> 1.3.5

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Thu Feb 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Initial build in Sisyphus

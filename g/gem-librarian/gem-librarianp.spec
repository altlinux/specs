%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname librarian

Name:          gem-librarian
Version:       0.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/librarian
Vcs:           https://github.com/voxpupuli/librarian.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(fakefs) >= 0.4.2
BuildRequires: gem(highline) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(thor) >= 0.15
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fakefs >= 0.4.2
%ruby_use_gem_dependency thor >= 0.15
Requires:      gem(fakefs) >= 0.4.2
Requires:      gem(highline) >= 0
Requires:      gem(thor) >= 0.15
Obsoletes:     gem-librarianp < %EVR
Provides:      gem-librarianp = %EVR
Provides:      gem(librarian) = 0.1.2

%description
Librarian is a framework for writing bundlers, which are tools that resolve,
fetch, install, and isolate a project's dependencies, in Ruby.

A bundler written with Librarian will expect you to provide a specfile listing
your project's declared dependencies, including any version constraints and
including the upstream sources for finding them. Librarian can resolve the spec,
write a lockfile listing the full resolution, fetch the resolved dependencies,
install them, and isolate them in your project.

A bundler written with Librarian will be similar in kind to Bundler, the bundler
for Ruby gems that many modern Rails applications use.


%if_enabled    doc
%package       -n gem-librarian-doc
Version:       0.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета librarian
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(librarian) = 0.1.2

%description   -n gem-librarian-doc
A Framework for Bundlers. Fork to support librarian-puppet documentation
files.

Librarian is a framework for writing bundlers, which are tools that resolve,
fetch, install, and isolate a project's dependencies, in Ruby.

A bundler written with Librarian will expect you to provide a specfile listing
your project's declared dependencies, including any version constraints and
including the upstream sources for finding them. Librarian can resolve the spec,
write a lockfile listing the full resolution, fetch the resolved dependencies,
install them, and isolate them in your project.

A bundler written with Librarian will be similar in kind to Bundler, the bundler
for Ruby gems that many modern Rails applications use.

%description   -n gem-librarian-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета librarian.
%endif


%if_enabled    devel
%package       -n gem-librarian-devel
Version:       0.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета librarian
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(librarian) = 0.1.2
Requires:      gem(fakefs) >= 0.4.2
Requires:      gem(highline) >= 0
Requires:      gem(json) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(thor) >= 0.15

%description   -n gem-librarian-devel
A Framework for Bundlers. Fork to support librarian-puppet development
package.

Librarian is a framework for writing bundlers, which are tools that resolve,
fetch, install, and isolate a project's dependencies, in Ruby.

A bundler written with Librarian will expect you to provide a specfile listing
your project's declared dependencies, including any version constraints and
including the upstream sources for finding them. Librarian can resolve the spec,
write a lockfile listing the full resolution, fetch the resolved dependencies,
install them, and isolate them in your project.

A bundler written with Librarian will be similar in kind to Bundler, the bundler
for Ruby gems that many modern Rails applications use.

%description   -n gem-librarian-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета librarian.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-librarian-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-librarian-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Wed Sep 23 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- ^ 1.1.2 -> 0.1.2
- * renamed package with subpackages

* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.1 -> 1.1.2

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.0 -> 1.1.1

* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.6.4 -> 1.0.0
- ! spec

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

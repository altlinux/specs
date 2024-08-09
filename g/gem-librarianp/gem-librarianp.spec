%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname librarianp

Name:          gem-librarianp
Version:       1.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/librarian
Vcs:           https://github.com/voxpupuli/librarian.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(fakefs) >= 1.0
BuildRequires: gem(github_changelog_generator) >= 1.16.4
BuildRequires: gem(thor) >= 1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(fakefs) >= 3
BuildConflicts: gem(thor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fakefs >= 2.5.0,fakefs < 3
Requires:      gem(thor) >= 1.0
Conflicts:     gem(thor) >= 2
Provides:      gem(librarianp) = 1.1.2


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
%package       -n gem-librarianp-doc
Version:       1.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета librarianp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(librarianp) = 1.1.2

%description   -n gem-librarianp-doc
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

%description   -n gem-librarianp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета librarianp.
%endif


%if_enabled    devel
%package       -n gem-librarianp-devel
Version:       1.1.2
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета librarianp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(librarianp) = 1.1.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(json) >= 0
Requires:      gem(fakefs) >= 1.0
Requires:      gem(github_changelog_generator) >= 1.16.4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(fakefs) >= 3

%description   -n gem-librarianp-devel
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

%description   -n gem-librarianp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета librarianp.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-librarianp-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-librarianp-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.1 -> 1.1.2

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.0 -> 1.1.1

* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.6.4 -> 1.0.0
- ! spec

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitar

Name:          gem-minitar
Version:       1.0.2
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitar/
Vcs:           https://github.com/halostatue/minitar/.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git2) >= 1.7
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 0.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(standard-minitest) >= 1.0
BuildRequires: gem(standard-thread_safety) >= 1.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(standard-minitest) >= 2
BuildConflicts: gem(standard-thread_safety) >= 2
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_ignore_names archive-tar-minitar
Obsoletes:     ruby-minitar < %EVR
Obsoletes:     ruby-archive-tar-minitar < %EVR
Provides:      ruby-minitar = %EVR
Provides:      ruby-archive-tar-minitar = %EVR
Provides:      gem(minitar) = 1.0.2


%description
The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.


%if_enabled    doc
%package       -n gem-minitar-doc
Version:       1.0.2
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitar) = 1.0.2
Obsoletes:     minitar-doc
Obsoletes:     ruby-archive-tar-minitar-doc
Provides:      minitar-doc
Provides:      ruby-archive-tar-minitar-doc

%description   -n gem-minitar-doc
Minimal pure-ruby support for POSIX tar(1) archives documentation files.

The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.

%description   -n gem-minitar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitar.
%endif


%if_enabled    devel
%package       -n gem-minitar-devel
Version:       1.0.2
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitar) = 1.0.2
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(base64) >= 0.2
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git2) >= 1.7
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 0.0
Requires:      gem(standard) >= 1.0
Requires:      gem(standard-minitest) >= 1.0
Requires:      gem(standard-thread_safety) >= 1.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(base64) >= 1
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2
Conflicts:     gem(standard-minitest) >= 2
Conflicts:     gem(standard-thread_safety) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-minitar-devel
Minimal pure-ruby support for POSIX tar(1) archives development package.

The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.

%description   -n gem-minitar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitar.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitar-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitar-devel
%doc README.rdoc
%endif


%changelog
* Sat Aug 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- ^ 0.9.0.1 -> 1.0.2

* Fri Oct 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0.1-alt1.1
- !spec

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0.1-alt1
- ^ 0.9 -> 0.9.0.1

* Tue Oct 29 2019 Pavel Skrylev <majioa@altlinux.org> 0.9-alt1
- update (^) 0.6.1 -> 0.9
- add (+) archive-tar-minitar gem and package deprecation

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

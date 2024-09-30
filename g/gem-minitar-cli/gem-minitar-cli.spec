%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitar-cli

Name:          gem-minitar-cli
Version:       1.0.0
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar}
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitar-cli/
Vcs:           https://github.com/halostatue/minitar-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git2) >= 1.7
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(minitar) >= 1.0.0
BuildRequires: gem(powerbar) >= 1.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(minitar) >= 1.1
BuildConflicts: gem(powerbar) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency powerbar >= 2.0.1,powerbar < 3
Requires:      gem(minitar) >= 1.0.0
Requires:      gem(powerbar) >= 1.0
Conflicts:     gem(minitar) >= 1.1
Conflicts:     gem(powerbar) >= 3
Provides:      gem(minitar-cli) = 1.0.0


%description
<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.8, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.


%package       -n minitar
Version:       1.0.0
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitar-cli
Group:         Other
BuildArch:     noarch

Requires:      gem(minitar-cli) = 1.0.0

%description   -n minitar
minitar-cli is a pure-Ruby command-line tool that uses {minitar}
executable(s).

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.8, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n minitar -l ru_RU.UTF-8
Исполнямка для самоцвета minitar-cli.


%if_enabled    doc
%package       -n gem-minitar-cli-doc
Version:       1.0.0
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitar-cli
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitar-cli) = 1.0.0

%description   -n gem-minitar-cli-doc
minitar-cli is a pure-Ruby command-line tool that uses {minitar} documentation
files.

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.8, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n gem-minitar-cli-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitar-cli.
%endif


%if_enabled    devel
%package       -n gem-minitar-cli-devel
Version:       1.0.0
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitar-cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitar-cli) = 1.0.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git2) >= 1.7
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(rake) >= 10.0
Requires:      gem(standard) >= 1.0
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rdoc) >= 7

%description   -n gem-minitar-cli-devel
minitar-cli is a pure-Ruby command-line tool that uses {minitar} development
package.

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.8, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n gem-minitar-cli-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitar-cli.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n minitar
%doc README.rdoc
%_bindir/minitar

%if_enabled    doc
%files         -n gem-minitar-cli-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitar-cli-devel
%doc README.rdoc
%endif


%changelog
* Thu Sep 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.8 -> 1.0.0

* Sat Oct 15 2022 Pavel Skrylev <majioa@altlinux.org> 0.8-alt0.1
- ^ 0.6.1 -> 0.8

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0

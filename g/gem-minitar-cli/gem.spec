%define        gemname minitar-cli

Name:          gem-minitar-cli
Version:       0.6.1
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar}
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitar-cli/
Vcs:           https://github.com/halostatue/minitar-cli/.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(minitar) >= 0.7.0 gem(minitar) < 1
BuildRequires: gem(powerbar) >= 1.0 gem(powerbar) < 3
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6
BuildRequires: gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
BuildRequires: gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
BuildRequires: gem(hoe-git) >= 1.6 gem(hoe-git) < 2
BuildRequires: gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
BuildRequires: gem(hoe-travis) >= 1.2 gem(hoe-travis) < 2
BuildRequires: gem(minitest-autotest) < 2 gem(minitest-autotest) >= 1.0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 0.0
BuildRequires: gem(hoe) >= 3.17 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency powerbar >= 2.0.1,powerbar < 3
%ruby_use_gem_dependency minitar >= 0.8,minitar < 1
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(minitar-cli) = 0.6.1


%description
<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.7, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.


%package       -n minitar
Version:       0.6.1
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitar-cli
Group:         Other
BuildArch:     noarch

Requires:      gem(minitar-cli) = 0.6.1

%description   -n minitar
minitar-cli is a pure-Ruby command-line tool that uses
{minitar} executable(s).

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.7, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n minitar -l ru_RU.UTF-8
Исполнямка для самоцвета minitar-cli.


%package       -n gem-minitar-cli-doc
Version:       0.6.1
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitar-cli
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitar-cli) = 0.6.1

%description   -n gem-minitar-cli-doc
minitar-cli is a pure-Ruby command-line tool that uses
{minitar}[https://github documentation files.

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.7, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n gem-minitar-cli-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitar-cli.


%package       -n gem-minitar-cli-devel
Version:       0.6.1
Release:       alt1
Summary:       minitar-cli is a pure-Ruby command-line tool that uses {minitar} development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitar-cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitar-cli) = 0.6.1
Requires:      gem(rdoc) >= 4.0

%description   -n gem-minitar-cli-devel
minitar-cli is a pure-Ruby command-line tool that uses
{minitar} development package.

<tt>minitar-cli</tt> is a pure-Ruby command-line tool that uses
{minitar}[https://github.com/halostatue/minitar] to provide a command-line tool,
+minitar+, for working with POSIX tar(1) archive files.

This is release 0.7, extracted from {minitar}[https://halostatue.ca/minitar],
with modernizations.

%description   -n gem-minitar-cli-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitar-cli.


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

%files         -n minitar
%doc README.rdoc
%_bindir/minitar

%files         -n gem-minitar-cli-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitar-cli-devel
%doc README.rdoc


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0

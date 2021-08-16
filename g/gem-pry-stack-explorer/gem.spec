%define        gemname pry-stack_explorer

Name:          gem-pry-stack-explorer
Version:       0.6.1
Release:       alt1
Summary:       Walk the stack in a Pry session
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pry/pry-stack_explorer
Vcs:           https://github.com/pry/pry-stack_explorer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(binding_of_caller) >= 1.0 gem(binding_of_caller) < 2
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rake) >= 0.9 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(binding_of_caller) >= 1.0 gem(binding_of_caller) < 2
Requires:      gem(pry) >= 0.13 gem(pry) < 1
Provides:      gem(pry-stack_explorer) = 0.6.1

%description
Walk the stack in a Pry session

Pry::StackExplorer is a plugin for Pry that allows navigating the call stack.

From the point a Pry session is started, the user can move up the stack through
parent frames, examine state, and even evaluate code.

Unlike ruby-debug, pry-stack_explorer incurs no runtime cost and enables
navigation right up the call-stack to the birth of the program.

The up, down, frame and stack commands are provided. See Pry's in-session help
for more information on any of these commands.


%package       -n gem-pry-stack-explorer-doc
Version:       0.6.1
Release:       alt1
Summary:       Walk the stack in a Pry session documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-stack_explorer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-stack_explorer) = 0.6.1

%description   -n gem-pry-stack-explorer-doc
Walk the stack in a Pry session documentation files.

Pry::StackExplorer is a plugin for Pry that allows navigating the call stack.

From the point a Pry session is started, the user can move up the stack through
parent frames, examine state, and even evaluate code.

Unlike ruby-debug, pry-stack_explorer incurs no runtime cost and enables
navigation right up the call-stack to the birth of the program.

The up, down, frame and stack commands are provided. See Pry's in-session help
for more information on any of these commands.

%description   -n gem-pry-stack-explorer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-stack_explorer.


%package       -n gem-pry-stack-explorer-devel
Version:       0.6.1
Release:       alt1
Summary:       Walk the stack in a Pry session development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-stack_explorer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-stack_explorer) = 0.6.1
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(rake) >= 0.9 gem(rake) < 14

%description   -n gem-pry-stack-explorer-devel
Walk the stack in a Pry session development package.

Pry::StackExplorer is a plugin for Pry that allows navigating the call stack.

From the point a Pry session is started, the user can move up the stack through
parent frames, examine state, and even evaluate code.

Unlike ruby-debug, pry-stack_explorer incurs no runtime cost and enables
navigation right up the call-stack to the birth of the program.

The up, down, frame and stack commands are provided. See Pry's in-session help
for more information on any of these commands.

%description   -n gem-pry-stack-explorer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-stack_explorer.


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

%files         -n gem-pry-stack-explorer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pry-stack-explorer-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0

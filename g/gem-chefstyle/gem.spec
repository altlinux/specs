%define        gemname chefstyle

Name:          gem-chefstyle
Version:       2.2.2
Release:       alt1
Summary:       RuboCop configuration for Chef's ruby projects
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chefstyle
Vcs:           https://github.com/chef/chefstyle.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Provides:      gem(chefstyle) = 2.2.2

%description
Chefstyle - Version Pinned RuboCop with Chef approved Cop list for linting.

This is an internal style guide for chef ruby projects (chef-client, ohai,
mixlib-shellout, mixlib-config, etc).

It is not meant for consumption by cookbooks or for any general purpose uses.
Chef Users and Customers Should Generally Not Use This Tool and Should Use
Cookstyle. It is not intended for any audience outside of chef core ruby
development.

It will conflict with rubocop defaults, cookstyle, finstyle and other ruby
style guides entirely by design. The point is that the core chef authors
vehemently disagree with them on points of style and this point is generally
not up for debate.

It will have many rules that are disabled simply because fixing a project as
large as chef-client would be tedious and have little value. It will have other
rules that are disabled because chef exposes edge conditions that make them
falsely alert. Other rules will be selected based on the biases of the core
chef developers which are often violently at odds with the rubocop core
developers over ruby style.

Pull requests to this repo will not be accepted without corresponding PRs into
at least the chef-client and ohai codebases to clean the code up. PRs will not
be accepted that assume unfunded mandates for other people to finish the work.
Do not open PRs offering opinions or suggestions without offering to do the
work.

The project itself is a derivative of finstyle, but starts with all rules
disabled. The active ruleset is in the config/chefstyle.yml file.


%package       -n chefstyle
Version:       2.2.2
Release:       alt1
Summary:       RuboCop configuration for Chef's ruby projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chefstyle
Group:         Other
BuildArch:     noarch

Requires:      gem(chefstyle) = 2.2.2

%description   -n chefstyle
RuboCop configuration for Chef's ruby projects executable(s).

Chefstyle - Version Pinned RuboCop with Chef approved Cop list for linting.

This is an internal style guide for chef ruby projects (chef-client, ohai,
mixlib-shellout, mixlib-config, etc).

It is not meant for consumption by cookbooks or for any general purpose uses.
Chef Users and Customers Should Generally Not Use This Tool and Should Use
Cookstyle. It is not intended for any audience outside of chef core ruby
development.

It will conflict with rubocop defaults, cookstyle, finstyle and other ruby
style guides entirely by design. The point is that the core chef authors
vehemently disagree with them on points of style and this point is generally
not up for debate.

It will have many rules that are disabled simply because fixing a project as
large as chef-client would be tedious and have little value. It will have other
rules that are disabled because chef exposes edge conditions that make them
falsely alert. Other rules will be selected based on the biases of the core
chef developers which are often violently at odds with the rubocop core
developers over ruby style.

Pull requests to this repo will not be accepted without corresponding PRs into
at least the chef-client and ohai codebases to clean the code up. PRs will not
be accepted that assume unfunded mandates for other people to finish the work.
Do not open PRs offering opinions or suggestions without offering to do the
work.

The project itself is a derivative of finstyle, but starts with all rules
disabled. The active ruleset is in the config/chefstyle.yml file.

%description   -n chefstyle -l ru_RU.UTF-8
Исполнямка для самоцвета chefstyle.


%package       -n gem-chefstyle-doc
Version:       2.2.2
Release:       alt1
Summary:       RuboCop configuration for Chef's ruby projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chefstyle
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chefstyle) = 2.2.2

%description   -n gem-chefstyle-doc
RuboCop configuration for Chef's ruby projects documentation files.

Chefstyle - Version Pinned RuboCop with Chef approved Cop list for linting.

This is an internal style guide for chef ruby projects (chef-client, ohai,
mixlib-shellout, mixlib-config, etc).

It is not meant for consumption by cookbooks or for any general purpose uses.
Chef Users and Customers Should Generally Not Use This Tool and Should Use
Cookstyle. It is not intended for any audience outside of chef core ruby
development.

It will conflict with rubocop defaults, cookstyle, finstyle and other ruby
style guides entirely by design. The point is that the core chef authors
vehemently disagree with them on points of style and this point is generally
not up for debate.

It will have many rules that are disabled simply because fixing a project as
large as chef-client would be tedious and have little value. It will have other
rules that are disabled because chef exposes edge conditions that make them
falsely alert. Other rules will be selected based on the biases of the core
chef developers which are often violently at odds with the rubocop core
developers over ruby style.

Pull requests to this repo will not be accepted without corresponding PRs into
at least the chef-client and ohai codebases to clean the code up. PRs will not
be accepted that assume unfunded mandates for other people to finish the work.
Do not open PRs offering opinions or suggestions without offering to do the
work.

The project itself is a derivative of finstyle, but starts with all rules
disabled. The active ruleset is in the config/chefstyle.yml file.

%description   -n gem-chefstyle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chefstyle.


%package       -n gem-chefstyle-devel
Version:       2.2.2
Release:       alt1
Summary:       RuboCop configuration for Chef's ruby projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chefstyle
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chefstyle) = 2.2.2

%description   -n gem-chefstyle-devel
RuboCop configuration for Chef's ruby projects development package.

Chefstyle - Version Pinned RuboCop with Chef approved Cop list for linting.

This is an internal style guide for chef ruby projects (chef-client, ohai,
mixlib-shellout, mixlib-config, etc).

It is not meant for consumption by cookbooks or for any general purpose uses.
Chef Users and Customers Should Generally Not Use This Tool and Should Use
Cookstyle. It is not intended for any audience outside of chef core ruby
development.

It will conflict with rubocop defaults, cookstyle, finstyle and other ruby
style guides entirely by design. The point is that the core chef authors
vehemently disagree with them on points of style and this point is generally
not up for debate.

It will have many rules that are disabled simply because fixing a project as
large as chef-client would be tedious and have little value. It will have other
rules that are disabled because chef exposes edge conditions that make them
falsely alert. Other rules will be selected based on the biases of the core
chef developers which are often violently at odds with the rubocop core
developers over ruby style.

Pull requests to this repo will not be accepted without corresponding PRs into
at least the chef-client and ohai codebases to clean the code up. PRs will not
be accepted that assume unfunded mandates for other people to finish the work.
Do not open PRs offering opinions or suggestions without offering to do the
work.

The project itself is a derivative of finstyle, but starts with all rules
disabled. The active ruleset is in the config/chefstyle.yml file.

%description   -n gem-chefstyle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chefstyle.


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

%files         -n chefstyle
%doc README.md
%_bindir/chefstyle

%files         -n gem-chefstyle-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chefstyle-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- + packaged gem with Ruby Policy 2.0

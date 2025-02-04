%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname uniform_notifier

Name:          gem-uniform-notifier
Version:       1.16.0
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/uniform_notifier
Vcs:           https://github.com/flyerhzm/uniform_notifier.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(rspec) > 0
BuildRequires: gem(slack-notifier) >= 1.0
BuildRequires: gem(xmpp4r) >= 0.5
BuildRequires: gem(rexml) >= 0
BuildConflicts: gem(xmpp4r) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency xmpp4r >= 0.5.6,xmpp4r < 1
%ruby_alias_names uniform_notifier,uniform-notifier
Requires:      ruby >= 2.3
Provides:      gem(uniform_notifier) = 1.16.0

%description
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp


%if_enabled    doc
%package       -n gem-uniform-notifier-doc
Version:       1.16.0
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uniform_notifier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uniform_notifier) = 1.16.0

%description   -n gem-uniform-notifier-doc
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp documentation files.

uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp

%description   -n gem-uniform-notifier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uniform_notifier.
%endif


%if_enabled    devel
%package       -n gem-uniform-notifier-devel
Version:       1.16.0
Release:       alt1
Summary:       uniform notifier for rails logger, customized logger, javascript alert, javascript console, growl and xmpp development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uniform_notifier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uniform_notifier) = 1.16.0
Requires:      gem(rake) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) > 0
Requires:      gem(slack-notifier) >= 1.0
Requires:      gem(xmpp4r) >= 0.5
Conflicts:     gem(xmpp4r) >= 1

%description   -n gem-uniform-notifier-devel
uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp development package.

uniform notifier for rails logger, customized logger, javascript alert,
javascript console, growl and xmpp

%description   -n gem-uniform-notifier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uniform_notifier.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-uniform-notifier-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-uniform-notifier-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Tue Feb 04 2025 Pavel Skrylev <majioa@altlinux.org> 1.16.0-alt1
- ^ 1.14.2 -> 1.16.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.14.2-alt1
- + packaged gem with Ruby Policy 2.0

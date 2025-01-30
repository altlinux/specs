%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname server_sent_events

Name:          gem-server-sent-events
Version:       0.1.3
Release:       alt1.1
Summary:       Library for dealing with server-sent events
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/xlab-si/server-sent-events-ruby
Vcs:           https://github.com/xlab-si/server-sent-events-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(yard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names server_sent_events,server-sent-events
Requires:      ruby >= 2.1
Provides:      gem(server_sent_events) = 0.1.3

%description
Library for dealing with server-sent events


%if_enabled    doc
%package       -n gem-server-sent-events-doc
Version:       0.1.3
Release:       alt1.1
Summary:       Library for dealing with server-sent events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета server_sent_events
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(server_sent_events) = 0.1.3

%description   -n gem-server-sent-events-doc
Library for dealing with server-sent events documentation files.

%description   -n gem-server-sent-events-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета server_sent_events.
%endif


%if_enabled    devel
%package       -n gem-server-sent-events-devel
Version:       0.1.3
Release:       alt1.1
Summary:       Library for dealing with server-sent events development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета server_sent_events
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(server_sent_events) = 0.1.3
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-server-sent-events-devel
Library for dealing with server-sent events development package.

%description   -n gem-server-sent-events-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета server_sent_events.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-server-sent-events-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-server-sent-events-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Jan 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1.1
- * refactor spec

* Mon Nov 08 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1
- + packaged gem with Ruby Policy 2.0

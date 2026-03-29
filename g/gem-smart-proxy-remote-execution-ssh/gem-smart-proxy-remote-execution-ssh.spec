%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname smart_proxy_remote_execution_ssh

Name:          gem-smart-proxy-remote-execution-ssh
Version:       1.0.2
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy
License:       GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_remote_execution_ssh
Vcs:           https://github.com/theforeman/smart_proxy_remote_execution_ssh.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bcrypt_pbkdf) >= 1.0
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(mocha) >= 2.0
BuildRequires: gem(mqtt) >= 0.5
BuildRequires: gem(net-ssh) >= 6.1.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(public_suffix) >= 0
BuildRequires: gem(rack) >= 1.1
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(smart_proxy) >= 0
BuildRequires: gem(smart_proxy_dynflow) >= 0.9.4
BuildRequires: gem(webmock) >= 1
BuildConflicts: gem(bcrypt_pbkdf) >= 2.0
BuildConflicts: gem(ed25519) >= 2.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(mqtt) >= 1
BuildConflicts: gem(net-ssh) >= 8
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(smart_proxy_dynflow) >= 2.0.0
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency net-ssh >= 6.1.0,net-ssh < 7
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 3
%ruby_alias_names smart_proxy_remote_execution_ssh,smart-proxy-remote-execution-ssh
Requires:      ruby >= 3.0
Requires:      gem(bcrypt_pbkdf) >= 1.0
Requires:      gem(ed25519) >= 1.2
Requires:      gem(mqtt) >= 0.5
Requires:      gem(net-ssh) >= 6.1.0
Requires:      gem(smart_proxy_dynflow) >= 0.9.4
Conflicts:     gem(bcrypt_pbkdf) >= 2.0
Conflicts:     gem(ed25519) >= 2.0
Conflicts:     gem(mqtt) >= 1
Conflicts:     gem(net-ssh) >= 8
Conflicts:     gem(smart_proxy_dynflow) >= 2.0.0
Provides:      gem(smart_proxy_remote_execution_ssh) = 1.0.2

%description
This a plugin for foreman smart-proxy allowing using ssh for the remote
execution.


%if_enabled    doc
%package       -n gem-smart-proxy-remote-execution-ssh-doc
Version:       1.0.2
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_remote_execution_ssh
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_remote_execution_ssh) = 1.0.2

%description   -n gem-smart-proxy-remote-execution-ssh-doc
Ssh remote execution provider for Foreman Smart-Proxy documentation files.

%description   -n gem-smart-proxy-remote-execution-ssh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_remote_execution_ssh.
%endif


%if_enabled    devel
%package       -n gem-smart-proxy-remote-execution-ssh-devel
Version:       1.0.2
Release:       alt1
Summary:       Ssh remote execution provider for Foreman Smart-Proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_remote_execution_ssh
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(smart_proxy_remote_execution_ssh) = 1.0.2
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(mocha) >= 2.0
Requires:      gem(pry) >= 0
Requires:      gem(public_suffix) >= 0
Requires:      gem(rack) >= 1.1
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(sinatra) >= 0
Requires:      gem(smart_proxy) >= 0
Requires:      gem(webmock) >= 1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(webmock) >= 4

%description   -n gem-smart-proxy-remote-execution-ssh-devel
Ssh remote execution provider for Foreman Smart-Proxy development package.

%description   -n gem-smart-proxy-remote-execution-ssh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_remote_execution_ssh.
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
%files         -n gem-smart-proxy-remote-execution-ssh-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-smart-proxy-remote-execution-ssh-devel
%doc LICENSE README.md
%endif


%changelog
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- ^ 0.4.1 -> 1.0.2

* Tue Nov 09 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0

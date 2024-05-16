%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname faye

Name:          gem-faye
Version:       1.4.0
Release:       alt1
Summary:       Simple pub/sub messaging for the web
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://faye.jcoglan.com
Vcs:           https://github.com/faye/faye.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(compass) >= 0.11.0
BuildRequires: gem(haml) >= 3.1.0
BuildRequires: gem(permessage_deflate) >= 0.1.0
BuildRequires: gem(puma) >= 2.0.0
BuildRequires: gem(rack-proxy) >= 0.4.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(RedCloth) >= 3.0.0
BuildRequires: gem(rspec) >= 2.99.0
BuildRequires: gem(rspec-eventmachine) >= 0.2.0
BuildRequires: gem(sass) >= 3.2.0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(staticmatic) >= 0
BuildRequires: gem(rainbows) >= 4.4.0
BuildRequires: gem(thin) >= 1.2.0
BuildRequires: gem(goliath) >= 0
BuildRequires: gem(passenger) >= 4.0.0
BuildRequires: gem(cookiejar) >= 0.3.0
BuildRequires: gem(em-http-request) >= 1.1.6
BuildRequires: gem(eventmachine) >= 0.12.0
BuildRequires: gem(faye-websocket) >= 0.11.0
BuildRequires: gem(multi_json) >= 1.0.0
BuildRequires: gem(rack) >= 1.0.0
BuildRequires: gem(websocket-driver) >= 0.5.1
BuildConflicts: gem(compass) >= 0.12
BuildConflicts: gem(haml) >= 7
BuildConflicts: gem(rack-proxy) >= 0.5
BuildConflicts: gem(RedCloth) >= 3.1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(sass) >= 3.3
BuildConflicts: gem(rainbows) >= 4.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency haml >= 6.1.1,haml < 7
Requires:      gem(cookiejar) >= 0.3.0
Requires:      gem(em-http-request) >= 1.1.6
Requires:      gem(eventmachine) >= 0.12.0
Requires:      gem(faye-websocket) >= 0.11.0
Requires:      gem(multi_json) >= 1.0.0
Requires:      gem(rack) >= 1.0.0
Requires:      gem(websocket-driver) >= 0.5.1
Provides:      gem(faye) = 1.4.0


%description
Faye is a set of tools for simple publish-subscribe messaging between web
clients. It ships with easy-to-use message routing servers for Node.js and Rack
applications, and clients that can be used on the server and in the browser.


%if_enabled    doc
%package       -n gem-faye-doc
Version:       1.4.0
Release:       alt1
Summary:       Simple pub/sub messaging for the web documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faye
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faye) = 1.4.0

%description   -n gem-faye-doc
Simple pub/sub messaging for the web documentation files.

Faye is a set of tools for simple publish-subscribe messaging between web
clients. It ships with easy-to-use message routing servers for Node.js and Rack
applications, and clients that can be used on the server and in the browser.

%description   -n gem-faye-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faye.
%endif


%if_enabled    devel
%package       -n gem-faye-devel
Version:       1.4.0
Release:       alt1
Summary:       Simple pub/sub messaging for the web development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faye
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faye) = 1.4.0
Requires:      gem(compass) >= 0.11.0
Requires:      gem(haml) >= 3.1.0
Requires:      gem(permessage_deflate) >= 0.1.0
Requires:      gem(puma) >= 2.0.0
Requires:      gem(rack-proxy) >= 0.4.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(RedCloth) >= 3.0.0
Requires:      gem(rspec) >= 2.99.0
Requires:      gem(rspec-eventmachine) >= 0.2.0
Requires:      gem(sass) >= 3.2.0
Requires:      gem(sinatra) >= 0
Requires:      gem(staticmatic) >= 0
Requires:      gem(rainbows) >= 4.4.0
Requires:      gem(thin) >= 1.2.0
Requires:      gem(goliath) >= 0
Requires:      gem(passenger) >= 4.0.0
Conflicts:     gem(compass) >= 0.12
Conflicts:     gem(haml) >= 7
Conflicts:     gem(rack-proxy) >= 0.5
Conflicts:     gem(RedCloth) >= 3.1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(sass) >= 3.3
Conflicts:     gem(rainbows) >= 4.5

%description   -n gem-faye-devel
Simple pub/sub messaging for the web development package.

Faye is a set of tools for simple publish-subscribe messaging between web
clients. It ships with easy-to-use message routing servers for Node.js and Rack
applications, and clients that can be used on the server and in the browser.

%description   -n gem-faye-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faye.
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
%files         -n gem-faye-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faye-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0

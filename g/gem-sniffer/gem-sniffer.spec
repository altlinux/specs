%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sniffer

Name:          gem-sniffer
Version:       0.5.0
Release:       alt1
Summary:       Analyze HTTP Requests
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/aderyabin/sniffer
Vcs:           https://github.com/aderyabin/sniffer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(puma) >= 3.10.0
BuildRequires: gem(httpclient) >= 2.8.3
BuildRequires: gem(http) >= 3.0.0
BuildRequires: gem(patron) >= 0.10.0
BuildRequires: gem(curb) >= 0.9.4
BuildRequires: gem(ethon) >= 0.11.0
BuildRequires: gem(typhoeus) >= 0.9.0
BuildRequires: gem(em-http-request) >= 1.1.0
BuildRequires: gem(excon) >= 0.60.0
BuildRequires: gem(anyway_config) >= 1.0
BuildRequires: gem(dry-initializer) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(dry-initializer) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency sinatra >= 4.0.0,sinatra < 5
Requires:      gem(anyway_config) >= 1.0
Requires:      gem(dry-initializer) >= 3
Conflicts:     gem(dry-initializer) >= 4
Provides:      gem(sniffer) = 0.5.0


%description
Analyze HTTP Requests. Sniffer aims to help:

* Log outgoing HTTP requests. Sniffer logs as JSON format for export to ELK,
  Logentries and etc;
* Debug requests. Sniffer allows to save all requests/responses in storage for
  future debugging;

Sniffer supports most common HTTP accessing libraries: Net::HTTP, HTTP,
HTTPClient, Patron, Curb, Ethon, Typhoeus, EM-HTTP-Request, Excon.


%if_enabled    doc
%package       -n gem-sniffer-doc
Version:       0.5.0
Release:       alt1
Summary:       Analyze HTTP Requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sniffer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sniffer) = 0.5.0

%description   -n gem-sniffer-doc
Analyze HTTP Requests documentation files.

Analyze HTTP Requests. Sniffer aims to help:

* Log outgoing HTTP requests. Sniffer logs as JSON format for export to ELK,
  Logentries and etc;
* Debug requests. Sniffer allows to save all requests/responses in storage for
  future debugging;

Sniffer supports most common HTTP accessing libraries: Net::HTTP, HTTP,
HTTPClient, Patron, Curb, Ethon, Typhoeus, EM-HTTP-Request, Excon.

%description   -n gem-sniffer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sniffer.
%endif


%if_enabled    devel
%package       -n gem-sniffer-devel
Version:       0.5.0
Release:       alt1
Summary:       Analyze HTTP Requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sniffer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sniffer) = 0.5.0
Requires:      gem(bundler) >= 2
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(sinatra) >= 2.0
Requires:      gem(puma) >= 3.10.0
Requires:      gem(httpclient) >= 2.8.3
Requires:      gem(http) >= 3.0.0
Requires:      gem(patron) >= 0.10.0
Requires:      gem(curb) >= 0.9.4
Requires:      gem(ethon) >= 0.11.0
Requires:      gem(typhoeus) >= 0.9.0
Requires:      gem(em-http-request) >= 1.1.0
Requires:      gem(excon) >= 0.60.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(sinatra) >= 5

%description   -n gem-sniffer-devel
Analyze HTTP Requests development package.

Analyze HTTP Requests. Sniffer aims to help:

* Log outgoing HTTP requests. Sniffer logs as JSON format for export to ELK,
  Logentries and etc;
* Debug requests. Sniffer allows to save all requests/responses in storage for
  future debugging;

Sniffer supports most common HTTP accessing libraries: Net::HTTP, HTTP,
HTTPClient, Patron, Curb, Ethon, Typhoeus, EM-HTTP-Request, Excon.

%description   -n gem-sniffer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sniffer.
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
%files         -n gem-sniffer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sniffer-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0

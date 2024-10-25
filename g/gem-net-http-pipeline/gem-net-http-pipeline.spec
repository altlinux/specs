%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-http-pipeline

Name:          gem-net-http-pipeline
Version:       1.0.1.4
Release:       alt1
Summary:       An HTTP/1.1 pipelining implementation atop Net::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-pipeline
Vcs:           https://github.com/drbrain/net-http-pipeline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Obsoletes:     ruby-net-http-pipeline < %EVR
Provides:      ruby-net-http-pipeline = %EVR
Provides:      gem(net-http-pipeline) = 1.0.1.4


%description
An HTTP/1.1 pipelining implementation atop Net::HTTP. A pipelined connection
sends multiple requests to the HTTP server without waiting for the responses.
The server will respond in-order.


%if_enabled    doc
%package       -n gem-net-http-pipeline-doc
Version:       1.0.1.4
Release:       alt1
Summary:       An HTTP/1.1 pipelining implementation atop Net::HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-http-pipeline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-http-pipeline) = 1.0.1.4

%description   -n gem-net-http-pipeline-doc
An HTTP/1.1 pipelining implementation atop Net::HTTP documentation files.

An HTTP/1.1 pipelining implementation atop Net::HTTP. A pipelined connection
sends multiple requests to the HTTP server without waiting for the responses.
The server will respond in-order.

%description   -n gem-net-http-pipeline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-http-pipeline.
%endif


%if_enabled    devel
%package       -n gem-net-http-pipeline-devel
Version:       1.0.1.4
Release:       alt1
Summary:       An HTTP/1.1 pipelining implementation atop Net::HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-http-pipeline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-http-pipeline) = 1.0.1.4
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-net-http-pipeline-devel
An HTTP/1.1 pipelining implementation atop Net::HTTP development package.

An HTTP/1.1 pipelining implementation atop Net::HTTP. A pipelined connection
sends multiple requests to the HTTP server without waiting for the responses.
The server will respond in-order.

%description   -n gem-net-http-pipeline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-http-pipeline.
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
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-net-http-pipeline-doc
%doc README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-http-pipeline-devel
%doc README.txt
%endif


%changelog
* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1.4-alt1
- ^ 1.0.1 -> 1.0.1.4

* Tue May 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt2.1
- ! spec tags and syntax

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

%define        gemname http_parser.rb

Name:          gem-http-parser-rb
Version:       0.8.0
Release:       alt1
Summary:       A simple callback-based HTTP request/response parser for writing http servers, clients and proxies
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tmm1/http_parser.rb
Vcs:           https://github.com/tmm1/http_parser.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         ruby-http-parser-rb.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libhttp-parser-devel 
BuildRequires: gem(rake-compiler) >= 1.0 gem(rake-compiler) < 2
BuildRequires: gem(rspec) >= 3 gem(rspec) < 4
BuildRequires: gem(json) >= 2.1 gem(json) < 3
BuildRequires: gem(benchmark_suite) >= 1.0 gem(benchmark_suite) < 2
BuildRequires: gem(ffi) >= 1.9 gem(ffi) < 2
BuildRequires: gem(yajl-ruby) >= 1.3 gem(yajl-ruby) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-http_parser.rb < %EVR
Provides:      ruby-http_parser.rb = %EVR
Provides:      gem(http_parser.rb) = 0.8.0


%description
Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java


%package       -n gem-http-parser-rb-doc
Version:       0.8.0
Release:       alt1
Summary:       A simple callback-based HTTP request/response parser for writing http servers, clients and proxies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http_parser.rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http_parser.rb) = 0.8.0

%description   -n gem-http-parser-rb-doc
A simple callback-based HTTP request/response parser for writing http servers,
clients and proxies documentation files.

Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java

%description   -n gem-http-parser-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http_parser.rb.


%package       -n gem-http-parser-rb-devel
Version:       0.8.0
Release:       alt1
Summary:       A simple callback-based HTTP request/response parser for writing http servers, clients and proxies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http_parser.rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http_parser.rb) = 0.8.0
Requires:      gem(rake-compiler) >= 1.0 gem(rake-compiler) < 2
Requires:      gem(rspec) >= 3 gem(rspec) < 4
Requires:      gem(json) >= 2.1 gem(json) < 3
Requires:      gem(benchmark_suite) >= 1.0 gem(benchmark_suite) < 2
Requires:      gem(ffi) >= 1.9 gem(ffi) < 2
Requires:      gem(yajl-ruby) >= 1.3 gem(yajl-ruby) < 2

%description   -n gem-http-parser-rb-devel
A simple callback-based HTTP request/response parser for writing http servers,
clients and proxies development package.

Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java

%description   -n gem-http-parser-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http_parser.rb.


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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-http-parser-rb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-http-parser-rb-devel
%doc README.md
%ruby_includedir/*


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.6.1 -> 0.8.0

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt3
- ! spec tags

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt2
- ! spec tags and syntax

* Thu Apr 25 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- > Ruby Policy 2.0
- > source from github
- ^ 0.6.0 -> 0.6.1

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.5
- Rebuild for new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt3
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt2
- Rebuild with Ruby 2.3.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for ALT Linux

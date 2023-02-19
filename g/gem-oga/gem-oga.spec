# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname oga

Name:          gem-oga
Version:       3.4
Release:       alt1
Summary:       Oga is an XML/HTML parser written in Ruby
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://gitlab.com/yorickpeterse/oga
Vcs:           https://gitlab.com/yorickpeterse/oga.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ragel6
BuildRequires: /usr/bin/ruby-ll
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(ruby-ll) >= 2.1
BuildConflicts: gem(ruby-ll) >= 3
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(ox) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(ast) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(benchmark-ips) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ast) >= 0
Requires:      gem(ruby-ll) >= 2.1
Conflicts:     gem(ruby-ll) >= 3
Provides:      gem(oga) = 3.4

%ruby_on_build_rake_tasks lexer,parser

%description
Oga is an XML/HTML parser written in Ruby. It provides an easy to use API for
parsing, modifying and querying documents (using XPath expressions). Oga does
not require system libraries such as libxml, making it easier and faster to
install on various platforms. To achieve better performance Oga uses a small,
native extension (C for MRI/Rubinius, Java for JRuby).

Oga provides an API that allows you to safely parse and query documents in a
multi-threaded environment, without having to worry about your applications
blowing up.


%package       -n gem-oga-doc
Version:       3.4
Release:       alt1
Summary:       Oga is an XML/HTML parser written in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oga
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oga) = 3.4

%description   -n gem-oga-doc
Oga is an XML/HTML parser written in Ruby documentation files.

Oga is an XML/HTML parser written in Ruby. It provides an easy to use API for
parsing, modifying and querying documents (using XPath expressions). Oga does
not require system libraries such as libxml, making it easier and faster to
install on various platforms. To achieve better performance Oga uses a small,
native extension (C for MRI/Rubinius, Java for JRuby).

Oga provides an API that allows you to safely parse and query documents in a
multi-threaded environment, without having to worry about your applications
blowing up.

%description   -n gem-oga-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oga.


%package       -n gem-oga-devel
Version:       3.4
Release:       alt1
Summary:       Oga is an XML/HTML parser written in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oga
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oga) = 3.4
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(yard) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(benchmark-ips) >= 2.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(ox) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      ragel6
Requires:      /usr/bin/ruby-ll
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(benchmark-ips) >= 3

%description   -n gem-oga-devel
Oga is an XML/HTML parser written in Ruby development package.

Oga is an XML/HTML parser written in Ruby. It provides an easy to use API for
parsing, modifying and querying documents (using XPath expressions). Oga does
not require system libraries such as libxml, making it easier and faster to
install on various platforms. To achieve better performance Oga uses a small,
native extension (C for MRI/Rubinius, Java for JRuby).

Oga provides an API that allows you to safely parse and query documents in a
multi-threaded environment, without having to worry about your applications
blowing up.

%description   -n gem-oga-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oga.


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
%ruby_gemextdir

%files         -n gem-oga-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-oga-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 3.4-alt1
- ^ 3.3 -> 3.4

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 3.3-alt1
- ^ 2.17 -> 3.3

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 2.17-alt1
- ^ 2.15 -> 2.17
- ! spec tag

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.15-alt1.1
- ! spec according to changelog rules

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.15-alt1
- + packaged as a gem with usage Ruby Policy 2.0

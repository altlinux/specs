%define        gemname rexml

Name:          gem-rexml
Version:       3.2.5
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/rexml
Vcs:           https://github.com/ruby/rexml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rexml) = 3.2.5


%description
REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.


%package       -n gem-rexml-doc
Version:       3.2.5
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rexml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rexml) = 3.2.5

%description   -n gem-rexml-doc
REXML is an XML toolkit for Ruby documentation files.

REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.

%description   -n gem-rexml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rexml.


%package       -n gem-rexml-devel
Version:       3.2.5
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rexml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rexml) = 3.2.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-rexml-devel
REXML is an XML toolkit for Ruby development package.

REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.

%description   -n gem-rexml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rexml.


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

%files         -n gem-rexml-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rexml-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.5-alt1
- ^ 3.2.4 -> 3.2.5

* Mon Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.4-alt1
- + packaged gem with usage Ruby Policy 2.0

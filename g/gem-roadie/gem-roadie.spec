%define        gemname roadie

Name:          gem-roadie
Version:       5.1.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Ruby rockstars
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Mange/roadie
Vcs:           https://github.com/mange/roadie.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-collection_matchers) >= 1.0 gem(rspec-collection_matchers) < 2
BuildRequires: gem(webmock) >= 3.0 gem(webmock) < 4
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(nokogiri) >= 1.8 gem(nokogiri) < 2
BuildRequires: gem(css_parser) >= 1.4 gem(css_parser) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 1.8 gem(nokogiri) < 2
Requires:      gem(css_parser) >= 1.4 gem(css_parser) < 2
Obsoletes:     ruby-roadie < %EVR
Provides:      ruby-roadie = %EVR
Provides:      gem(roadie) = 5.1.0


%description
Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you inside your emails.


%package       -n gem-roadie-doc
Version:       5.1.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Ruby rockstars documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета roadie
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(roadie) = 5.1.0

%description   -n gem-roadie-doc
Making HTML emails comfortable for the Ruby rockstars documentation
files.

Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you inside your emails.

%description   -n gem-roadie-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета roadie.


%package       -n gem-roadie-devel
Version:       5.1.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Ruby rockstars development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета roadie
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(roadie) = 5.1.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-collection_matchers) >= 1.0 gem(rspec-collection_matchers) < 2
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4
Requires:      gem(codecov) >= 0
Requires:      gem(standard) >= 0

%description   -n gem-roadie-devel
Making HTML emails comfortable for the Ruby rockstars development
package.

Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you inside your emails.

%description   -n gem-roadie-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета roadie.


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

%files         -n gem-roadie-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-roadie-devel
%doc README.md


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- ^ 4.0.0 -> 5.1.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- updated (^) 3.5.0 -> 4.0.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- updated (^) 3.4.0 -> 3.5.0
- moved (>) Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- added (+) initial gemified build for Sisyphus

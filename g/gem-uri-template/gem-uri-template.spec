%define        gemname uri_template

Name:          gem-uri-template
Version:       0.7.0
Release:       alt1
Summary:       A templating system for URIs
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/hannesg/uri_template
Vcs:           https://github.com/hannesg/uri_template.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(escape_utils) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(mutant) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(addressable) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(uri_template) = 0.7.0


%description
A templating system for URIs, which implements RFC6570 and Colon based
URITemplates in a clean and straight forward way.


%package       -n gem-uri-template-doc
Version:       0.7.0
Release:       alt1
Summary:       A templating system for URIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uri_template
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uri_template) = 0.7.0

%description   -n gem-uri-template-doc
A templating system for URIs documentation files.

A templating system for URIs, which implements RFC6570 and Colon based
URITemplates in a clean and straight forward way.

%description   -n gem-uri-template-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uri_template.


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

%files         -n gem-uri-template-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0

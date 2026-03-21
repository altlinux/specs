%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname protocol-url

Name:          gem-protocol-url
Version:       0.4.0
Release:       alt1
Summary:       Provides abstractions for working with URLs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-url
Vcs:           https://github.com/socketry/protocol-url.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      gem(protocol-url) = 0.4.0

%description
Provides abstractions for working with URLs.


%if_enabled    doc
%package       -n gem-protocol-url-doc
Version:       0.4.0
Release:       alt1
Summary:       Provides abstractions for working with URLs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-url
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(protocol-url) = 0.4.0

%description   -n gem-protocol-url-doc
Provides abstractions for working with URLs documentation files.

%description   -n gem-protocol-url-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-url.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-protocol-url-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

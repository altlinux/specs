%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname io-stream

Name:          gem-io-stream
Version:       0.11.1
Release:       alt1
Summary:       Provides a generic stream wrapper for IO instances
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/io-stream
Vcs:           https://github.com/socketry/io-stream.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      gem(io-stream) = 0.11.1

%description
Provides a generic stream wrapper for IO instances.

Provide a buffered stream implementation for Ruby, independent of the underlying
IO.


%if_enabled    doc
%package       -n gem-io-stream-doc
Version:       0.11.1
Release:       alt1
Summary:       Provides a generic stream wrapper for IO instances documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-stream
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(io-stream) = 0.11.1

%description   -n gem-io-stream-doc
Provides a generic stream wrapper for IO instances documentation files.

Provide a buffered stream implementation for Ruby, independent of the underlying
IO.

%description   -n gem-io-stream-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-stream.
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
%files         -n gem-io-stream-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.11.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname base64

Name:          gem-base64
Version:       0.2.0
Release:       alt1
Summary:       Support for encoding and decoding binary data using a Base64 representation
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/base64
Vcs:           https://github.com/ruby/base64.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(base64) = 0.2.0


%description
Support for encoding and decoding binary data using a Base64 representation.


%if_enabled    doc
%package       -n gem-base64-doc
Version:       0.2.0
Release:       alt1
Summary:       Support for encoding and decoding binary data using a Base64 representation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета base64
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(base64) = 0.2.0

%description   -n gem-base64-doc
Support for encoding and decoding binary data using a Base64 representation
documentation files.

%description   -n gem-base64-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета base64.
%endif


%if_enabled    devel
%package       -n gem-base64-devel
Version:       0.2.0
Release:       alt1
Summary:       Support for encoding and decoding binary data using a Base64 representation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета base64
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(base64) = 0.2.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-base64-devel
Support for encoding and decoding binary data using a Base64 representation
development package.

%description   -n gem-base64-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета base64.
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
%files         -n gem-base64-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-base64-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0

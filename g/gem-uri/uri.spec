%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname uri

Name:          gem-uri
Version:       1.1.1
Release:       alt1
Summary:       URI is a module providing classes to handle Uniform Resource Identifiers
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/uri
Vcs:           https://github.com/ruby/uri.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 1.0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5
Provides:      gem(uri) = 1.1.1

%description
URI is a module providing classes to handle Uniform Resource Identifiers


%if_enabled    doc
%package       -n gem-uri-doc
Version:       1.1.1
Release:       alt1
Summary:       URI is a module providing classes to handle Uniform Resource Identifiers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uri
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(uri) = 1.1.1

%description   -n gem-uri-doc
URI is a module providing classes to handle Uniform Resource Identifiers
documentation files.

%description   -n gem-uri-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uri.
%endif


%if_enabled    devel
%package       -n gem-uri-devel
Version:       1.1.1
Release:       alt1
Summary:       URI is a module providing classes to handle Uniform Resource Identifiers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uri
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(uri) = 1.1.1
Requires:      gem(bundler) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 1.0.7

%description   -n gem-uri-devel
URI is a module providing classes to handle Uniform Resource Identifiers
development package.

%description   -n gem-uri-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uri.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-uri-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-uri-devel
%doc COPYING README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

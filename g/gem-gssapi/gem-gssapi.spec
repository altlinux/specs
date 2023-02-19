%define        gemname gssapi

Name:          gem-gssapi
Version:       1.3.1
Release:       alt1.1
Summary:       A Ruby FFI wrapper around GSSAPI
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zenchild/gssapi
Vcs:           https://github.com/zenchild/gssapi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(ffi) >= 1.0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.0.1
Provides:      gem(gssapi) = 1.3.1


%description
This is a wrapper around the system GSSAPI library (MIT only at this time). It
exposes the low-level GSSAPI methods like gss_init_sec_context and gss_wrap and
also provides an easier to use wrapper on top of this for common usage
scenarios.

I'm going to try and maintain most of the docs in the Github WIKI for this
project so please check there for documentation and
examples.

https://github.com/zenchild/gssapi/wiki

Also check out the examples directory for some stubbed out client/server
examples.


%package       -n gem-gssapi-doc
Version:       1.3.1
Release:       alt1.1
Summary:       A Ruby FFI wrapper around GSSAPI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gssapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gssapi) = 1.3.1

%description   -n gem-gssapi-doc
A Ruby FFI wrapper around GSSAPI documentation files.

This is a wrapper around the system GSSAPI library (MIT only at this time). It
exposes the low-level GSSAPI methods like gss_init_sec_context and gss_wrap and
also provides an easier to use wrapper on top of this for common usage
scenarios.

I'm going to try and maintain most of the docs in the Github WIKI for this
project so please check there for documentation and
examples.

https://github.com/zenchild/gssapi/wiki

Also check out the examples directory for some stubbed out client/server
examples.

%description   -n gem-gssapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gssapi.


%package       -n gem-gssapi-devel
Version:       1.3.1
Release:       alt1.1
Summary:       A Ruby FFI wrapper around GSSAPI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gssapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gssapi) = 1.3.1
Requires:      gem(pry-byebug) >= 0

%description   -n gem-gssapi-devel
A Ruby FFI wrapper around GSSAPI development package.

This is a wrapper around the system GSSAPI library (MIT only at this time). It
exposes the low-level GSSAPI methods like gss_init_sec_context and gss_wrap and
also provides an easier to use wrapper on top of this for common usage
scenarios.

I'm going to try and maintain most of the docs in the Github WIKI for this
project so please check there for documentation and
examples.

https://github.com/zenchild/gssapi/wiki

Also check out the examples directory for some stubbed out client/server
examples.

%description   -n gem-gssapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gssapi.


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

%files         -n gem-gssapi-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gssapi-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1.1
- ! closes build deps under check condition

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- ^ 1.2.0 -> 1.3.1

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0

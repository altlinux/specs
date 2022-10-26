%define        gemname introspection

Name:          gem-introspection
Version:       0.0.4
Release:       alt1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object
License:       MIT
Group:         Development/Ruby
Url:           http://jamesmead.org
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(blankslate) >= 0
BuildRequires: gem(metaclass) >= 0.0.1 gem(metaclass) < 0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(metaclass) >= 0.0.1 gem(metaclass) < 0.1
Provides:      gem(introspection) = 0.0.4

%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object.


%package       -n gem-introspection-doc
Version:       0.0.4
Release:       alt1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета introspection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(introspection) = 0.0.4

%description   -n gem-introspection-doc
Dynamic inspection of the hierarchy of method definitions on a Ruby object
documentation files.

%description   -n gem-introspection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета introspection.


%package       -n gem-introspection-devel
Version:       0.0.4
Release:       alt1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(introspection) = 0.0.4
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(rake) >= 0
Requires:      gem(blankslate) >= 0

%description   -n gem-introspection-devel
Dynamic inspection of the hierarchy of method definitions on a Ruby object
development package.

%description   -n gem-introspection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета introspection.


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

%files         -n gem-introspection-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-introspection-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0

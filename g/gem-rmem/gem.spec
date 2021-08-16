%define        gemname rmem

Name:          gem-rmem
Version:       1.0.0
Release:       alt1
Summary:       Ruby Memory Measurebindings
License:       Ruby
Group:         Development/Ruby

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rmem) = 1.0.0


%description
Measure approximate process memory.


%package       -n gem-rmem-doc
Version:       1.0.0
Release:       alt1
Summary:       Ruby Memory Measurebindings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rmem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rmem) = 1.0.0

%description   -n gem-rmem-doc
Ruby Memory Measurebindings documentation files.

Measure approximate process memory.

%description   -n gem-rmem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rmem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-rmem-doc
%doc README
%ruby_gemdocdir


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0

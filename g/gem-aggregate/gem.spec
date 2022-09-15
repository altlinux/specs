%define        gemname aggregate

Name:          gem-aggregate
Version:       0.2.3
Release:       alt1
Summary:       Aggregate is a Ruby class for accumulating aggregate statistics and includes histogram support
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/josephruscio/aggregate
Vcs:           https://github.com/josephruscio/aggregate.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(aggregate) = 0.2.3

%ruby_use_gem_version aggregate:0.2.3

%description
Aggregate is an intuitive ruby implementation of a statistics aggregator
including both default and configurable histogram support. It does this
without recording/storing any of the actual sample values, making it
suitable for tracking statistics across millions/billions of sample
without any impact on performance or memory footprint. Originally
inspired by the Aggregate support in SystemTap.


%package       -n gem-aggregate-doc
Version:       0.2.3
Release:       alt1
Summary:       Aggregate is a Ruby class for accumulating aggregate statistics and includes histogram support documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aggregate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aggregate) = 0.2.3

%description   -n gem-aggregate-doc
Aggregate is a Ruby class for accumulating aggregate statistics and includes
histogram support documentation files.

Aggregate is an intuitive ruby implementation of a statistics aggregator
including both default and configurable histogram support. It does this
without recording/storing any of the actual sample values, making it
suitable for tracking statistics across millions/billions of sample
without any impact on performance or memory footprint. Originally
inspired by the Aggregate support in SystemTap.

%description   -n gem-aggregate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aggregate.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-aggregate-doc
%ruby_gemdocdir


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0

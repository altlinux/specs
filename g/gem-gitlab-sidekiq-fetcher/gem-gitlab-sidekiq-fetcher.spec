%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gitlab-sidekiq-fetcher

Name:          gem-gitlab-sidekiq-fetcher
Version:       0.9.0
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq
License:       LGPL-3.0
Group:         Development/Ruby
Url:           https://gitlab.com/gitlab-org/sidekiq-reliable-fetch/
Vcs:           https://gitlab.com/gitlab-org/sidekiq-reliable-fetch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sidekiq) >= 6.1
BuildRequires: gem(stub_env) >= 1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(sidekiq) >= 8
BuildConflicts: gem(stub_env) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency sidekiq >= 7.3.8,sidekiq < 8
Requires:      gem(json) >= 2.3.0
Requires:      gem(sidekiq) >= 6.1
Conflicts:     gem(sidekiq) >= 8
Provides:      gem(gitlab-sidekiq-fetcher) = 0.9.0

%description
gitlab-sidekiq-fetcher is an extension to Sidekiq that adds support for reliable
fetches from Redis.

It's based on https://github.com/TEA-ebook/sidekiq-reliable-fetch.

There are two strategies implemented: Reliable fetch using rpoplpush command and
semi-reliable fetch that uses regular brpop and lpush to pick the job and put it
to working queue. The main benefit of "Reliable" strategy is that rpoplpush is
atomic, eliminating a race condition in which jobs can be lost. However, it
comes at a cost because rpoplpush can't watch multiple lists at the same time so
we need to iterate over the entire queue list which significantly increases
pressure on Redis when there are more than a few queues. The "semi-reliable"
strategy is much more reliable than the default Sidekiq fetcher, though.
Compared to the reliable fetch strategy, it does not increase pressure on Redis
significantly.


%if_enabled    doc
%package       -n gem-gitlab-sidekiq-fetcher-doc
Version:       0.9.0
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gitlab-sidekiq-fetcher
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gitlab-sidekiq-fetcher) = 0.9.0

%description   -n gem-gitlab-sidekiq-fetcher-doc
Redis reliable queue pattern implemented in Sidekiq documentation
files.

gitlab-sidekiq-fetcher is an extension to Sidekiq that adds support for reliable
fetches from Redis.

It's based on https://github.com/TEA-ebook/sidekiq-reliable-fetch.

There are two strategies implemented: Reliable fetch using rpoplpush command and
semi-reliable fetch that uses regular brpop and lpush to pick the job and put it
to working queue. The main benefit of "Reliable" strategy is that rpoplpush is
atomic, eliminating a race condition in which jobs can be lost. However, it
comes at a cost because rpoplpush can't watch multiple lists at the same time so
we need to iterate over the entire queue list which significantly increases
pressure on Redis when there are more than a few queues. The "semi-reliable"
strategy is much more reliable than the default Sidekiq fetcher, though.
Compared to the reliable fetch strategy, it does not increase pressure on Redis
significantly.

%description   -n gem-gitlab-sidekiq-fetcher-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gitlab-sidekiq-fetcher.
%endif


%if_enabled    devel
%package       -n gem-gitlab-sidekiq-fetcher-devel
Version:       0.9.0
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gitlab-sidekiq-fetcher
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gitlab-sidekiq-fetcher) = 0.9.0
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(simplecov) >= 0
Requires:      gem(stub_env) >= 1.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(stub_env) >= 2

%description   -n gem-gitlab-sidekiq-fetcher-devel
Redis reliable queue pattern implemented in Sidekiq development
package.

gitlab-sidekiq-fetcher is an extension to Sidekiq that adds support for reliable
fetches from Redis.

It's based on https://github.com/TEA-ebook/sidekiq-reliable-fetch.

There are two strategies implemented: Reliable fetch using rpoplpush command and
semi-reliable fetch that uses regular brpop and lpush to pick the job and put it
to working queue. The main benefit of "Reliable" strategy is that rpoplpush is
atomic, eliminating a race condition in which jobs can be lost. However, it
comes at a cost because rpoplpush can't watch multiple lists at the same time so
we need to iterate over the entire queue list which significantly increases
pressure on Redis when there are more than a few queues. The "semi-reliable"
strategy is much more reliable than the default Sidekiq fetcher, though.
Compared to the reliable fetch strategy, it does not increase pressure on Redis
significantly.

%description   -n gem-gitlab-sidekiq-fetcher-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gitlab-sidekiq-fetcher.
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
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gitlab-sidekiq-fetcher-doc
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gitlab-sidekiq-fetcher-devel
%doc CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.8.0 -> 0.9.0

* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.5.2 -> 0.8.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- added (+) packaged gem with usage Ruby Policy 2.0

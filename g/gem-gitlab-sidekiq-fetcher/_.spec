%define        gemname gitlab-sidekiq-fetcher

Name:          gem-gitlab-sidekiq-fetcher
Version:       0.8.0
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
BuildRequires: gem(sidekiq) >= 6.1 gem(sidekiq) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sidekiq) >= 6.1 gem(sidekiq) < 7
Provides:      gem(gitlab-sidekiq-fetcher) = 0.8.0


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


%package       -n gem-gitlab-sidekiq-fetcher-doc
Version:       0.8.0
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gitlab-sidekiq-fetcher
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gitlab-sidekiq-fetcher) = 0.8.0

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


%package       -n gem-gitlab-sidekiq-fetcher-devel
Version:       0.8.0
Release:       alt1
Summary:       Redis reliable queue pattern implemented in Sidekiq development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gitlab-sidekiq-fetcher
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gitlab-sidekiq-fetcher) = 0.8.0

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

%files         -n gem-gitlab-sidekiq-fetcher-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gitlab-sidekiq-fetcher-devel
%doc README.md


%changelog
* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.5.2 -> 0.8.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.2-alt1
- added (+) packaged gem with usage Ruby Policy 2.0

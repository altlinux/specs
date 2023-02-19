%define        gemname remix-stash

Name:          gem-remix-stash
Version:       1.1.5
Release:       alt1.1
Summary:       Remix your memcache
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/binary42/remix-stash
Vcs:           https://github.com/binary42/remix-stash.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rails) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(remix-stash) = 1.1.5


%description
New API that doesn't actually suck! I've rethought a lot of the API and this
comes with a lot of new capabilities. More work is being done on making it as
expressive as possible without terrible overhead. This includes vectorized keys
which allow emulation of partial cache clearing as well as nice shortcuts like
eval and gate for expressions. Options, clusters, and implicit scope are easy to
manage on a stash-by-stash basis. Keys are also easy to pass in as it will
create composite keys from whatever you pass in (as long as it has to_s) so no
more ugly string interpolation all over the place.

It's fast (faster than memcache-client). It's simple (pure ruby and only a few
hundred lines). It's tested (shoulda). Of course, because it's pure ruby it will
run almost anywhere as well unlike many other clients.

It does require memcached 1.4+ but you should be running that anyway (if you
aren't, upgrade already).


%package       -n gem-remix-stash-doc
Version:       1.1.5
Release:       alt1.1
Summary:       Remix your memcache documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета remix-stash
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(remix-stash) = 1.1.5

%description   -n gem-remix-stash-doc
Remix your memcache documentation files.

New API that doesn't actually suck! I've rethought a lot of the API and this
comes with a lot of new capabilities. More work is being done on making it as
expressive as possible without terrible overhead. This includes vectorized keys
which allow emulation of partial cache clearing as well as nice shortcuts like
eval and gate for expressions. Options, clusters, and implicit scope are easy to
manage on a stash-by-stash basis. Keys are also easy to pass in as it will
create composite keys from whatever you pass in (as long as it has to_s) so no
more ugly string interpolation all over the place.

It's fast (faster than memcache-client). It's simple (pure ruby and only a few
hundred lines). It's tested (shoulda). Of course, because it's pure ruby it will
run almost anywhere as well unlike many other clients.

It does require memcached 1.4+ but you should be running that anyway (if you
aren't, upgrade already).

%description   -n gem-remix-stash-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета remix-stash.


%package       -n gem-remix-stash-devel
Version:       1.1.5
Release:       alt1.1
Summary:       Remix your memcache development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета remix-stash
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(remix-stash) = 1.1.5
Requires:      gem(rails) >= 0

%description   -n gem-remix-stash-devel
Remix your memcache development package.

New API that doesn't actually suck! I've rethought a lot of the API and this
comes with a lot of new capabilities. More work is being done on making it as
expressive as possible without terrible overhead. This includes vectorized keys
which allow emulation of partial cache clearing as well as nice shortcuts like
eval and gate for expressions. Options, clusters, and implicit scope are easy to
manage on a stash-by-stash basis. Keys are also easy to pass in as it will
create composite keys from whatever you pass in (as long as it has to_s) so no
more ugly string interpolation all over the place.

It's fast (faster than memcache-client). It's simple (pure ruby and only a few
hundred lines). It's tested (shoulda). Of course, because it's pure ruby it will
run almost anywhere as well unlike many other clients.

It does require memcached 1.4+ but you should be running that anyway (if you
aren't, upgrade already).

%description   -n gem-remix-stash-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета remix-stash.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-remix-stash-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-remix-stash-devel
%doc README.markdown


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1.1
- ! closes build deps under check condition

* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- + packaged gem with Ruby Policy 2.0

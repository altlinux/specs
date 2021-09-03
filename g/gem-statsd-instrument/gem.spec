%define        gemname statsd-instrument

Name:          gem-statsd-instrument
Version:       3.1.1
Release:       alt1
Summary:       A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD instrumentation into your code
License:       MIT
Group:         Development/Ruby
Url:           http://shopify.github.io/statsd-instrument/
Vcs:           https://github.com/shopify/statsd-instrument.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(concurrent-ruby) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(statsd-instrument) = 3.1.1


%description
This is a ruby client for statsd (http://github.com/etsy/statsd). It provides a
lightweight way to track and measure metrics in your application.

We call out to statsd by sending data over a UDP socket. UDP sockets are fast,
but unreliable, there is no guarantee that your data will ever arrive at its
location. In other words, fire and forget. This is perfect for this use case
because it means your code doesn't get bogged down trying to log statistics. We
send data to statsd several times per request and haven't noticed a performance
hit.

For more information about StatsD, see the README of the Etsy project.


%package       -n gem-statsd-instrument-doc
Version:       3.1.1
Release:       alt1
Summary:       A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD instrumentation into your code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета statsd-instrument
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(statsd-instrument) = 3.1.1

%description   -n gem-statsd-instrument-doc
A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD
instrumentation into your code documentation files.

This is a ruby client for statsd (http://github.com/etsy/statsd). It provides a
lightweight way to track and measure metrics in your application.

We call out to statsd by sending data over a UDP socket. UDP sockets are fast,
but unreliable, there is no guarantee that your data will ever arrive at its
location. In other words, fire and forget. This is perfect for this use case
because it means your code doesn't get bogged down trying to log statistics. We
send data to statsd several times per request and haven't noticed a performance
hit.

For more information about StatsD, see the README of the Etsy project.

%description   -n gem-statsd-instrument-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета statsd-instrument.


%package       -n gem-statsd-instrument-devel
Version:       3.1.1
Release:       alt1
Summary:       A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD instrumentation into your code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета statsd-instrument
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(statsd-instrument) = 3.1.1
Requires:      gem(concurrent-ruby) >= 0

%description   -n gem-statsd-instrument-devel
A StatsD client for Ruby apps. Provides metaprogramming methods to inject StatsD
instrumentation into your code development package.

This is a ruby client for statsd (http://github.com/etsy/statsd). It provides a
lightweight way to track and measure metrics in your application.

We call out to statsd by sending data over a UDP socket. UDP sockets are fast,
but unreliable, there is no guarantee that your data will ever arrive at its
location. In other words, fire and forget. This is perfect for this use case
because it means your code doesn't get bogged down trying to log statistics. We
send data to statsd several times per request and haven't noticed a performance
hit.

For more information about StatsD, see the README of the Etsy project.

%description   -n gem-statsd-instrument-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета statsd-instrument.


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

%files         -n gem-statsd-instrument-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-statsd-instrument-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 2.4.0 -> 3.1.1

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- updated to (^) v2.4.0
- fix (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

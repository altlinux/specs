%define        gemname sinatra

Name:          gem-sinatra
Epoch:         1
Version:       2.1.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL
License:       MIT
Group:         Development/Ruby
Url:           http://www.sinatrarb.com/
Vcs:           https://github.com/sinatra/sinatra.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(mustermann) >= 1.0 gem(mustermann) < 2
BuildRequires: gem(tilt) >= 2.0 gem(tilt) < 3
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(haml) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(erubis) >= 0
BuildRequires: gem(slim) >= 0
BuildRequires: gem(less) >= 0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(liquid) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(RedCloth) >= 4.2.9 gem(RedCloth) < 5
BuildRequires: gem(asciidoctor) >= 0
BuildRequires: gem(radius) >= 0
BuildRequires: gem(coffee-script) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(creole) >= 0
BuildRequires: gem(wikicloth) >= 0
BuildRequires: gem(markaby) >= 0
BuildRequires: gem(rake) >= 13.0.1 gem(rake) < 14
BuildRequires: gem(rack) >= 2.2 gem(rack) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency RedCloth >= 4.3.2,RedCloth < 5
Requires:      gem(rack) >= 2.2 gem(rack) < 3
Requires:      gem(tilt) >= 2.0 gem(tilt) < 3
Requires:      gem(rack-protection) = 2.1.0
Requires:      gem(mustermann) >= 1.0 gem(mustermann) < 2
Obsoletes:     ruby-sinatra < %EVR
Provides:      ruby-sinatra = %EVR
Provides:      gem(sinatra) = 2.1.0


%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package       -n gem-rack-protection
Version:       2.1.0
Release:       alt1
Summary:       This gem protects against typical web attacks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) >= 0 gem(rack) < 3
Obsoletes:     ruby-rack-protection < %EVR
Provides:      ruby-rack-protection = %EVR
Provides:      gem(rack-protection) = 2.1.0

%description   -n gem-rack-protection
This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.


%package       -n gem-rack-protection-doc
Version:       2.1.0
Release:       alt1
Summary:       This gem protects against typical web attacks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-protection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-protection) = 2.1.0

%description   -n gem-rack-protection-doc
This gem protects against typical web attacks documentation files.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.

%description   -n gem-rack-protection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-protection.


%package       -n gem-rack-protection-devel
Version:       2.1.0
Release:       alt1
Summary:       This gem protects against typical web attacks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-protection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-protection) = 2.1.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-rack-protection-devel
This gem protects against typical web attacks development package.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.

%description   -n gem-rack-protection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-protection.


%package       -n gem-sinatra-contrib
Version:       2.1.0
Release:       alt1
Summary:       Collection of common Sinatra extensions, semi-officially supported
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sinatra) = 2.1.0
Requires:      gem(mustermann) >= 1.0 gem(mustermann) < 2
Requires:      gem(tilt) >= 2.0 gem(tilt) < 3
Requires:      gem(rack-protection) = 2.1.0
Requires:      gem(multi_json) >= 0
Provides:      gem(sinatra-contrib) = 2.1.0

%description   -n gem-sinatra-contrib
Collection of common Sinatra extensions, semi-officially supported:
- sinatra/capture: Let's you capture the content of blocks in templates.
- sinatra/config_file: Allows loading configuration from yaml files.
- sinatra/content_for: Adds Rails-style content_for helpers to Haml, Erb, Erubis
and Slim.
- sinatra/cookies: A cookies helper for reading and writing cookies.
- sinatra/engine_tracking: Adds methods like haml? that allow helper methods to
check whether they are called from within a template.
- sinatra/json: Adds a #json helper method to return JSON documents.
- sinatra/link_header: Helpers for generating link HTML tags and corresponding
Link HTTP headers. Adds link, stylesheet and prefetch helper methods.
- sinatra/multi_route: Adds ability to define one route block for multiple
routes and multiple or custom HTTP verbs.
- sinatra/namespace: Adds namespace support to Sinatra.
- sinatra/respond_with: Choose action and/or template automatically depending on
the incoming request. Adds helpers respond_to and respond_with.
- sinatra/custom_logger: This extension allows you to define your own logger
instance using +logger+ setting. That logger then will be available as #logger
helper method in your routes and views.
- sinatra/required_params: Ensure if required query parameters exist


%package       -n gem-sinatra-contrib-doc
Version:       2.1.0
Release:       alt1
Summary:       Collection of common Sinatra extensions, semi-officially supported documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra-contrib
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra-contrib) = 2.1.0

%description   -n gem-sinatra-contrib-doc
Collection of common Sinatra extensions, semi-officially supported documentation
files.

Collection of common Sinatra extensions, semi-officially supported:
- sinatra/capture: Let's you capture the content of blocks in templates.
- sinatra/config_file: Allows loading configuration from yaml files.
- sinatra/content_for: Adds Rails-style content_for helpers to Haml, Erb, Erubis
and Slim.
- sinatra/cookies: A cookies helper for reading and writing cookies.
- sinatra/engine_tracking: Adds methods like haml? that allow helper methods to
check whether they are called from within a template.
- sinatra/json: Adds a #json helper method to return JSON documents.
- sinatra/link_header: Helpers for generating link HTML tags and corresponding
Link HTTP headers. Adds link, stylesheet and prefetch helper methods.
- sinatra/multi_route: Adds ability to define one route block for multiple
routes and multiple or custom HTTP verbs.
- sinatra/namespace: Adds namespace support to Sinatra.
- sinatra/respond_with: Choose action and/or template automatically depending on
the incoming request. Adds helpers respond_to and respond_with.
- sinatra/custom_logger: This extension allows you to define your own logger
instance using +logger+ setting. That logger then will be available as #logger
helper method in your routes and views.
- sinatra/required_params: Ensure if required query parameters exist

%description   -n gem-sinatra-contrib-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sinatra-contrib.


%package       -n gem-sinatra-contrib-devel
Version:       2.1.0
Release:       alt1
Summary:       Collection of common Sinatra extensions, semi-officially supported development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sinatra-contrib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sinatra-contrib) = 2.1.0
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(haml) >= 0
Requires:      gem(erubi) >= 0
Requires:      gem(erubis) >= 0
Requires:      gem(slim) >= 0
Requires:      gem(less) >= 0
Requires:      gem(sass) >= 0
Requires:      gem(builder) >= 0
Requires:      gem(liquid) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(RedCloth) >= 4.2.9 gem(RedCloth) < 5
Requires:      gem(asciidoctor) >= 0
Requires:      gem(radius) >= 0
Requires:      gem(coffee-script) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(creole) >= 0
Requires:      gem(wikicloth) >= 0
Requires:      gem(markaby) >= 0
Requires:      gem(rake) >= 13.0.1 gem(rake) < 14
Requires:      gem(rack-test) >= 0

%description   -n gem-sinatra-contrib-devel
Collection of common Sinatra extensions, semi-officially supported development
package.

Collection of common Sinatra extensions, semi-officially supported:
- sinatra/capture: Let's you capture the content of blocks in templates.
- sinatra/config_file: Allows loading configuration from yaml files.
- sinatra/content_for: Adds Rails-style content_for helpers to Haml, Erb, Erubis
and Slim.
- sinatra/cookies: A cookies helper for reading and writing cookies.
- sinatra/engine_tracking: Adds methods like haml? that allow helper methods to
check whether they are called from within a template.
- sinatra/json: Adds a #json helper method to return JSON documents.
- sinatra/link_header: Helpers for generating link HTML tags and corresponding
Link HTTP headers. Adds link, stylesheet and prefetch helper methods.
- sinatra/multi_route: Adds ability to define one route block for multiple
routes and multiple or custom HTTP verbs.
- sinatra/namespace: Adds namespace support to Sinatra.
- sinatra/respond_with: Choose action and/or template automatically depending on
the incoming request. Adds helpers respond_to and respond_with.
- sinatra/custom_logger: This extension allows you to define your own logger
instance using +logger+ setting. That logger then will be available as #logger
helper method in your routes and views.
- sinatra/required_params: Ensure if required query parameters exist

%description   -n gem-sinatra-contrib-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sinatra-contrib.


%package       -n gem-sinatra-doc
Version:       2.1.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra) = 2.1.0

%description   -n gem-sinatra-doc
Classy web-development dressed in a DSL documentation files.

Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.

%description   -n gem-sinatra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sinatra.


%package       -n gem-sinatra-devel
Version:       2.1.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sinatra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sinatra) = 2.1.0

%description   -n gem-sinatra-devel
Classy web-development dressed in a DSL development package.

Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.

%description   -n gem-sinatra-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sinatra.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.de.md README.es.md README.fr.md README.hu.md README.ja.md README.ko.md README.malayalam.md README.md README.pt-br.md README.pt-pt.md README.ru.md README.zh.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rack-protection
%doc README.md
%ruby_gemspecdir/rack-protection-2.1.0.gemspec
%ruby_gemslibdir/rack-protection-2.1.0

%files         -n gem-rack-protection-doc
%doc README.md
%ruby_gemsdocdir/rack-protection-2.1.0

%files         -n gem-rack-protection-devel
%doc README.md

%files         -n gem-sinatra-contrib
%doc README.md
%ruby_gemspecdir/sinatra-contrib-2.1.0.gemspec
%ruby_gemslibdir/sinatra-contrib-2.1.0

%files         -n gem-sinatra-contrib-doc
%doc README.md
%ruby_gemsdocdir/sinatra-contrib-2.1.0

%files         -n gem-sinatra-contrib-devel
%doc README.md

%files         -n gem-sinatra-doc
%doc README.de.md README.es.md README.fr.md README.hu.md README.ja.md README.ko.md README.malayalam.md README.md README.pt-br.md README.pt-pt.md README.ru.md README.zh.md
%ruby_gemdocdir

%files         -n gem-sinatra-devel
%doc README.de.md README.es.md README.fr.md README.hu.md README.ja.md README.ko.md README.malayalam.md README.md README.pt-br.md README.pt-pt.md README.ru.md README.zh.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.1.0-alt1
- ^ 2.0.5 -> 2.1.0

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.5-alt1
- Bump to 2.0.5
- Use Ruby Policy 2.0

* Mon Nov 12 2018 Alexey Shabalin <shaba@altlinux.org> 1:2.0.4-alt1
- 2.0.4

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Jun 20 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.4.8-alt1
- Downgrade version to work with old ruby-rack

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt2
- Build with ruby-rack 1.x

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

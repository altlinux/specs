%define        gemname sinatra

Name:          gem-sinatra
Epoch:         1
Version:       2.2.3
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
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(rack-test) >= 0.6.2
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(twitter-text) = 1.14.7
BuildRequires: gem(activesupport) >= 5.1.6
BuildRequires: gem(less) >= 2.0
BuildRequires: gem(therubyracer) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(wlang) >= 3.0.1
BuildRequires: gem(bluecloth) >= 0
BuildRequires: gem(rdiscount) >= 0
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(puma) >= 5
BuildRequires: gem(yajl-ruby) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rainbows) >= 0
BuildRequires: gem(eventmachine) >= 0
BuildRequires: gem(slim) >= 2.0
BuildRequires: gem(coffee-script) >= 2.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(maruku) >= 0
BuildRequires: gem(creole) >= 0
BuildRequires: gem(wikicloth) >= 0
BuildRequires: gem(markaby) >= 0
BuildRequires: gem(radius) >= 0
BuildRequires: gem(asciidoctor) >= 0
BuildRequires: gem(liquid) >= 0
BuildRequires: gem(stylus) >= 0
BuildRequires: gem(rabl) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(erubis) >= 0
BuildRequires: gem(haml) >= 3.0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(reel-rack) >= 0
BuildRequires: gem(celluloid) >= 0.16.0
BuildRequires: gem(commonmarker) >= 0.20.0
BuildRequires: gem(pandoc-ruby) >= 2.0.2
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(tilt) >= 2.0
BuildRequires: gem(mustermann) >= 2.0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rspec) >= 3.6
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(haml) >= 5
BuildRequires: gem(less) >= 0
BuildRequires: gem(RedCloth) >= 4.2.9
BuildRequires: gem(coffee-script) >= 0
BuildRequires: gem(execjs) = 2.0.0
BuildRequires: gem(nokogiri) = 1.5.10
BuildRequires: gem(redcarpet) = 2.3.0
BuildRequires: gem(ref) >= 0
BuildRequires: gem(multi_json) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(activesupport) >= 7
BuildConflicts: gem(less) >= 3
BuildConflicts: gem(puma) >= 6
BuildConflicts: gem(slim) >= 3
BuildConflicts: gem(celluloid) >= 0.17
BuildConflicts: gem(commonmarker) >= 0.21
BuildConflicts: gem(pandoc-ruby) >= 2.1
BuildConflicts: gem(tilt) >= 3
BuildConflicts: gem(mustermann) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(haml) >= 6
BuildConflicts: gem(RedCloth) >= 4.3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(liquid) > 2.6.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_dependency mustermann >= 3.0.0,mustermann < 4
Requires:      gem(rack) >= 2.2.2
Requires:      gem(tilt) >= 2.0
Requires:      gem(rack-protection) = 2.2.3
Requires:      gem(mustermann) >= 2.0
Conflicts:     gem(tilt) >= 3
Conflicts:     gem(mustermann) >= 4
Obsoletes:     ruby-sinatra < %EVR
Provides:      ruby-sinatra = %EVR
Provides:      gem(sinatra) = 2.2.3


%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package       -n gem-rack-protection
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) >= 0
Obsoletes:     ruby-rack-protection < %EVR
Provides:      ruby-rack-protection = %EVR
Provides:      gem(rack-protection) = 2.2.3

%description   -n gem-rack-protection
This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.


%package       -n gem-rack-protection-doc
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-protection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-protection) = 2.2.3

%description   -n gem-rack-protection-doc
Classy web-development dressed in a DSL documentation files.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.

%description   -n gem-rack-protection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-protection.


%package       -n gem-rack-protection-devel
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-protection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-protection) = 2.2.3
Requires:      gem(rake) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rspec) >= 3.6
Conflicts:     gem(rspec) >= 4

%description   -n gem-rack-protection-devel
Classy web-development dressed in a DSL development package.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.

%description   -n gem-rack-protection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-protection.


%package       -n gem-sinatra-contrib
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(multi_json) >= 0
Requires:      gem(sinatra) = 2.2.3
Requires:      gem(mustermann) >= 2.0
Requires:      gem(tilt) >= 2.0
Requires:      gem(rack-protection) = 2.2.3
Conflicts:     gem(mustermann) >= 4
Conflicts:     gem(tilt) >= 3
Provides:      gem(sinatra-contrib) = 2.2.3

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
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra-contrib
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra-contrib) = 2.2.3

%description   -n gem-sinatra-contrib-doc
Classy web-development dressed in a DSL documentation files.

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


%package       -n gem-sinatra-doc
Version:       2.2.3
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra) = 2.2.3

%description   -n gem-sinatra-doc
Classy web-development dressed in a DSL documentation files.

Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.

%description   -n gem-sinatra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sinatra.


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
%ruby_gemspecdir/rack-protection-2.2.3.gemspec
%ruby_gemslibdir/rack-protection-2.2.3

%files         -n gem-rack-protection-doc
%doc README.md
%ruby_gemsdocdir/rack-protection-2.2.3

%files         -n gem-sinatra-contrib
%doc README.md
%ruby_gemspecdir/sinatra-contrib-2.2.3.gemspec
%ruby_gemslibdir/sinatra-contrib-2.2.3

%files         -n gem-sinatra-contrib-doc
%doc README.md
%ruby_gemsdocdir/sinatra-contrib-2.2.3

%files         -n gem-sinatra-doc
%doc README.de.md README.es.md README.fr.md README.hu.md README.ja.md README.ko.md README.malayalam.md README.md README.pt-br.md README.pt-pt.md README.ru.md README.zh.md
%ruby_gemdocdir


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1:2.2.3-alt1
- ^ 2.1.0 -> 2.2.3 (no devel)

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

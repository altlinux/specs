%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname sinatra

Name:          gem-sinatra
Epoch:         1
Version:       4.0.0
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
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(rack-session) >= 2.0.0
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(asciidoctor) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(childprocess) >= 5
BuildRequires: gem(commonmarker) >= 0.23.4
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(eventmachine) >= 0
BuildRequires: gem(falcon) >= 0.40
BuildRequires: gem(haml) >= 6
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(liquid) >= 0
BuildRequires: gem(markaby) >= 0
BuildRequires: gem(nokogiri) > 1.5.0
BuildRequires: gem(pandoc-ruby) >= 2.0.2
BuildRequires: gem(rabl) >= 0
BuildRequires: gem(rdiscount) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(slim) >= 4
BuildRequires: gem(yajl-ruby) >= 0
BuildRequires: gem(zeitwerk) >= 0
BuildRequires: gem(sass-embedded) >= 1.54
BuildRequires: gem(mustermann) >= 3.0
BuildRequires: gem(tilt) >= 2.0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(base64) >= 0.1.0
BuildRequires: gem(haml) >= 0
BuildRequires: gem(hamlit) >= 3
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(slim) >= 0
BuildRequires: gem(multi_json) >= 0.0.2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rack-session) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(commonmarker) >= 0.24
BuildConflicts: gem(falcon) >= 1
BuildConflicts: gem(haml) >= 7
BuildConflicts: gem(pandoc-ruby) >= 3
BuildConflicts: gem(slim) >= 5
BuildConflicts: gem(sass-embedded) >= 2
BuildConflicts: gem(mustermann) >= 4
BuildConflicts: gem(tilt) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency tilt < 3
%ruby_use_gem_dependency pandoc-ruby < 3
Requires:      gem(rack) >= 2.2.2
Requires:      gem(rack-session) >= 2.0.0
Requires:      gem(mustermann) >= 3.0
Requires:      gem(rack-protection) = 4.0.0
Requires:      gem(tilt) >= 2.0
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rack-session) >= 3
Conflicts:     gem(mustermann) >= 4
Conflicts:     gem(tilt) >= 3
Obsoletes:     ruby-sinatra < %EVR
Provides:      ruby-sinatra = %EVR
Provides:      gem(sinatra) = 4.0.0


%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.


%package       -n gem-rack-protection
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack) >= 2.2.2
Requires:      gem(base64) >= 0.1.0
Conflicts:     gem(rack) >= 4
Obsoletes:     ruby-rack-protection < %EVR
Provides:      ruby-rack-protection = %EVR
Provides:      gem(rack-protection) = 4.0.0

%description   -n gem-rack-protection
This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.


%if_enabled    doc
%package       -n gem-rack-protection-doc
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-protection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-protection) = 4.0.0

%description   -n gem-rack-protection-doc
Classy web-development dressed in a DSL documentation files.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.
%description   -n gem-rack-protection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-protection.
%endif


%if_enabled    devel
%package       -n gem-rack-protection-devel
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-protection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-protection) = 4.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(rack-test) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-rack-protection-devel
Classy web-development dressed in a DSL development package.

This gem protects against typical web attacks. Should work for all Rack apps,
including Rails.
%description   -n gem-rack-protection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-protection.
%endif


%package       -n gem-sinatra-contrib
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tilt) >= 0
Requires:      gem(multi_json) >= 0.0.2
Requires:      gem(mustermann) >= 3.0
Requires:      gem(rack-protection) = 4.0.0
Requires:      gem(sinatra) = 4.0.0
Conflicts:     gem(tilt) >= 3
Conflicts:     gem(mustermann) >= 4
Provides:      gem(sinatra-contrib) = 4.0.0

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


%if_enabled    doc
%package       -n gem-sinatra-contrib-doc
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra-contrib
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra-contrib) = 4.0.0

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
%endif


%if_enabled    devel
%package       -n gem-sinatra-contrib-devel
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sinatra-contrib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sinatra-contrib) = 4.0.0
Requires:      gem(erubi) >= 0
Requires:      gem(haml) >= 0
Requires:      gem(hamlit) >= 3
Requires:      gem(rack) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3
Requires:      gem(slim) >= 0
Requires:      gem(yajl-ruby) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-sinatra-contrib-devel
Classy web-development dressed in a DSL development package.

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
%endif


%if_enabled    doc
%package       -n gem-sinatra-doc
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sinatra
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sinatra) = 4.0.0

%description   -n gem-sinatra-doc
Classy web-development dressed in a DSL documentation files.

Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.
%description   -n gem-sinatra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sinatra.
%endif


%if_enabled    devel
%package       -n gem-sinatra-devel
Version:       4.0.0
Release:       alt1
Summary:       Classy web-development dressed in a DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sinatra
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sinatra) = 4.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rackup) >= 0
Requires:      gem(puma) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(yard) >= 0
Requires:      gem(asciidoctor) >= 0
Requires:      gem(builder) >= 0
Requires:      gem(childprocess) >= 5
Requires:      gem(commonmarker) >= 0.23.4
Requires:      gem(erubi) >= 0
Requires:      gem(eventmachine) >= 0
Requires:      gem(falcon) >= 0.40
Requires:      gem(haml) >= 6
Requires:      gem(kramdown) >= 0
Requires:      gem(liquid) >= 0
Requires:      gem(markaby) >= 0
Requires:      gem(nokogiri) > 1.5.0
Requires:      gem(pandoc-ruby) >= 2.0.2
Requires:      gem(rabl) >= 0
Requires:      gem(rdiscount) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(slim) >= 4
Requires:      gem(yajl-ruby) >= 0
Requires:      gem(zeitwerk) >= 0
Requires:      gem(sass-embedded) >= 1.54
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(commonmarker) >= 0.24
Conflicts:     gem(falcon) >= 1
Conflicts:     gem(haml) >= 7
Conflicts:     gem(pandoc-ruby) >= 3
Conflicts:     gem(slim) >= 5
Conflicts:     gem(sass-embedded) >= 2

%description   -n gem-sinatra-devel
Classy web-development dressed in a DSL development package.

Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.
%description   -n gem-sinatra-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sinatra.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rack-protection
%doc README.md
%ruby_gemspecdir/rack-protection-4.0.0.gemspec
%ruby_gemslibdir/rack-protection-4.0.0

%if_enabled    doc
%files         -n gem-rack-protection-doc
%doc README.md
%ruby_gemsdocdir/rack-protection-4.0.0
%endif

%if_enabled    devel
%files         -n gem-rack-protection-devel
%doc README.md
%endif

%files         -n gem-sinatra-contrib
%doc README.md
%ruby_gemspecdir/sinatra-contrib-4.0.0.gemspec
%ruby_gemslibdir/sinatra-contrib-4.0.0

%if_enabled    doc
%files         -n gem-sinatra-contrib-doc
%doc README.md
%ruby_gemsdocdir/sinatra-contrib-4.0.0
%endif

%if_enabled    devel
%files         -n gem-sinatra-contrib-devel
%doc README.md
%endif

%if_enabled    doc
%files         -n gem-sinatra-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sinatra-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1:4.0.0-alt1
- ^ 2.2.4 -> 4.0.0

* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1:2.2.4-alt1
- ^ 2.2.3 -> 2.2.4 (no devel)

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

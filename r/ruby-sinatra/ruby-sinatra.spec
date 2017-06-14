%define  pkgname sinatra
%define  sdir    %ruby_sitelibdir/%pkgname

Name: 	 ruby-%pkgname
Version: 2.0.0 
Release: alt1

Summary: Classy web-development dressed in a DSL
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/sinatra/sinatra

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package -n ruby-rack-protection
Summary: This gem protects against typical web attacks
Group:   Development/Ruby

%description -n ruby-rack-protection
This gem protects against typical web attacks. Should work for all Rack
apps, including Rails.

%package contrib
Summary: Collection of common Sinatra extensions, semi-officially supported
Group:   Development/Ruby

%description contrib
Collection of common Sinatra extensions, semi-officially supported:
- sinatra/capture: Let's you capture the content of blocks in templates.
- sinatra/config_file: Allows loading configuration from yaml files.
- sinatra/content_for: Adds Rails-style content_for helpers to Haml,
  Erb, Erubis and Slim.
- sinatra/cookies: A cookies helper for reading and writing cookies.
- sinatra/engine_tracking: Adds methods like haml? that allow helper
  methods to check whether they are called from within a template.
- sinatra/json: Adds a #json helper method to return JSON documents.
- sinatra/link_header: Helpers for generating link HTML tags and
  corresponding Link HTTP headers. Adds link, stylesheet and prefetch
  helper methods.
- sinatra/multi_route: Adds ability to define one route block for
  multiple routes and multiple or custom HTTP verbs.
- sinatra/namespace: Adds namespace support to Sinatra.
- sinatra/respond_with: Choose action and/or template automatically
  depending on the incoming request. Adds helpers respond_to and
  respond_with.
- sinatra/custom_logger: This extension allows you to define your own
  logger instance using +logger+ setting. That logger then will be
  available as #logger helper method in your routes and views.
- sinatra/required_params: Ensure if required query parameters exist

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
for dir in . rack-protection sinatra-contrib; do
	pushd "$dir"
	%update_setup_rb
	popd
done

%build
for dir in . rack-protection sinatra-contrib; do
	pushd "$dir"
	%ruby_config
	%ruby_build
	popd
done

%install
for dir in . rack-protection sinatra-contrib; do
	pushd "$dir"
	%ruby_install
	%rdoc lib/
	popd
done

# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%sdir.rb
%sdir
%exclude %sdir/capture*
%exclude %sdir/config_file*
%exclude %sdir/content_for*
%exclude %sdir/cookies*
%exclude %sdir/engine_tracking*
%exclude %sdir/json*
%exclude %sdir/link_header*
%exclude %sdir/multi_route*
%exclude %sdir/namespace*
%exclude %sdir/respond_with*
%exclude %sdir/custom_logger*
%exclude %sdir/required_params*

%files -n ruby-rack-protection
%doc rack-protection/*.md
%ruby_sitelibdir/rack-protection.rb
%ruby_sitelibdir/rack/protection*

%files contrib
%doc sinatra-contrib/*.md
%sdir/capture*
%sdir/config_file*
%sdir/content_for*
%sdir/cookies*
%sdir/engine_tracking*
%sdir/json*
%sdir/link_header*
%sdir/multi_route*
%sdir/namespace*
%sdir/respond_with*
%sdir/custom_logger*
%sdir/required_params*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

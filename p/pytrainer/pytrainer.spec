%define _unpackaged_files_terminate_build 1

%def_with check

Name: pytrainer
Version: 2.2.1
Release: alt1

Summary: desktop application for logging sport activities
License: GPL-2.0-or-later
Group: Office
URL: https://github.com/pytrainer/pytrainer

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: perl-Math-BigInt

%if_with check
BuildRequires: python3(sqlalchemy)
BuildRequires: python3(lxml)
BuildRequires: python3(matplotlib)
BuildRequires: python3(contourpy)
BuildRequires: python3-module-fonttools
%endif

%filter_from_requires /python3(urllib2)/d

Requires: gpsbabel

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Pytrainer is a desktop application for logging and graphing sporting
activities such as running or cycling sessions. Data can be imported from
GPS devices, files or input manually. Currently pytrainer supports GPX,
TCX and FIT files.

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Office;Calendar;Chart;Viewer;|" pytrainer.desktop

%build
%pyproject_build

%install
%pyproject_install

%find_lang %name

%check
#%%tox_create_default_config
%tox_check_pyproject

%files -f %{name}.lang
%doc COPYING INSTALL PLUGINS.README README.md
%_bindir/pytrainer
%_desktopdir/pytrainer.desktop
%_pixmapsdir/pytrainer.png
%dir %_datadir/pytrainer
%dir %_datadir/pytrainer/extensions
%dir %_datadir/pytrainer/extensions/fixelevation
%_datadir/pytrainer/extensions/fixelevation/README.txt
%_datadir/pytrainer/extensions/fixelevation/conf.xml
%_datadir/pytrainer/extensions/fixelevation/fixelevation.py
%dir %_datadir/pytrainer/extensions/gpx2garmin
%_datadir/pytrainer/extensions/gpx2garmin/README
%_datadir/pytrainer/extensions/gpx2garmin/conf.xml
%_datadir/pytrainer/extensions/gpx2garmin/gpx2garmin.py
%dir %_datadir/pytrainer/extensions/openstreetmap
%_datadir/pytrainer/extensions/openstreetmap/OSM_AnonSelection.glade
%_datadir/pytrainer/extensions/openstreetmap/README.txt
%_datadir/pytrainer/extensions/openstreetmap/conf.xml
%_datadir/pytrainer/extensions/openstreetmap/openstreetmap.py
%dir %_datadir/pytrainer/extensions/stravaupload
%_datadir/pytrainer/extensions/stravaupload/README
%_datadir/pytrainer/extensions/stravaupload/__init__.py
%_datadir/pytrainer/extensions/stravaupload/conf.xml
%_datadir/pytrainer/extensions/stravaupload/stravaupload.py
%_datadir/pytrainer/extensions/stravaupload/test_strava.py
%dir %_datadir/pytrainer/extensions/wordpress
%_datadir/pytrainer/extensions/wordpress/README.txt
%_datadir/pytrainer/extensions/wordpress/conf.xml
%_datadir/pytrainer/extensions/wordpress/wordpress.py
%_datadir/pytrainer/extensions/wordpress/wordpresslib.py
%dir %_datadir/pytrainer/glade
%_datadir/pytrainer/glade/equipment.ui
%_datadir/pytrainer/glade/extensions.ui
%_datadir/pytrainer/glade/finish.png
%_datadir/pytrainer/glade/glasses.png
%_datadir/pytrainer/glade/graph.png
%_datadir/pytrainer/glade/heartrate.png
%_datadir/pytrainer/glade/hr-bars.png
%_datadir/pytrainer/glade/hr-graph.png
%_datadir/pytrainer/glade/hr-queso.png
%_datadir/pytrainer/glade/importdata.ui
%_datadir/pytrainer/glade/logo.png
%_datadir/pytrainer/glade/logo_mini.png
%_datadir/pytrainer/glade/map.png
%_datadir/pytrainer/glade/newrecord.ui
%_datadir/pytrainer/glade/plugins.ui
%_datadir/pytrainer/glade/profile.ui
%_datadir/pytrainer/glade/pytrainer.ui
%_datadir/pytrainer/glade/pytrainer_mini.png
%_datadir/pytrainer/glade/selecttrackdialog.ui
%_datadir/pytrainer/glade/start.png
%_datadir/pytrainer/glade/summit.png
%_datadir/pytrainer/glade/trigger_distance.png
%_datadir/pytrainer/glade/trigger_hr.png
%_datadir/pytrainer/glade/trigger_location.png
%_datadir/pytrainer/glade/trigger_manual.png
%_datadir/pytrainer/glade/trigger_time.png
%_datadir/pytrainer/glade/waypoint.png
%dir %_datadir/pytrainer/imports
%_datadir/pytrainer/imports/__init__.py
%_datadir/pytrainer/imports/file_garminfit.py
%_datadir/pytrainer/imports/file_garmintcxv1.py
%_datadir/pytrainer/imports/file_garmintcxv2.py
%_datadir/pytrainer/imports/file_garmintools.py
%_datadir/pytrainer/imports/file_gpxplus.py
%_datadir/pytrainer/imports/file_gpxplusNokia.py
%_datadir/pytrainer/imports/file_kml20.py
%_datadir/pytrainer/imports/tool_gant.py
%_datadir/pytrainer/imports/tool_garmintools.py
%_datadir/pytrainer/imports/tool_gpsbabel.py
%_datadir/pytrainer/imports/translate_garmintcxv1.xsl
%_datadir/pytrainer/imports/translate_garmintcxv2.xsl
%_datadir/pytrainer/imports/translate_garmintools.xsl
%dir %_datadir/pytrainer/plugins
%dir %_datadir/pytrainer/plugins/garmin-fit
%dir %_datadir/pytrainer/plugins/garmin-fit/bin
%dir %_datadir/pytrainer/plugins/garmin-fit/bin/Geo
%_datadir/pytrainer/plugins/garmin-fit/bin/Geo/FIT.pm
%_datadir/pytrainer/plugins/garmin-fit/bin/fit2tcx.pl
%_datadir/pytrainer/plugins/garmin-fit/conf.xml
%_datadir/pytrainer/plugins/garmin-fit/garmin-fit.py
%_datadir/pytrainer/plugins/garmin-fit/translate.xsl
%dir %_datadir/pytrainer/plugins/garmin-gpx
%_datadir/pytrainer/plugins/garmin-gpx/conf.xml
%_datadir/pytrainer/plugins/garmin-gpx/garmingpx.py
%dir %_datadir/pytrainer/plugins/garmin-hr-file
%_datadir/pytrainer/plugins/garmin-hr-file/conf.xml
%_datadir/pytrainer/plugins/garmin-hr-file/garminhrfile.py
%_datadir/pytrainer/plugins/garmin-hr-file/pytrainer.style
%_datadir/pytrainer/plugins/garmin-hr-file/translate.xsl
%dir %_datadir/pytrainer/plugins/garmin-hr
%_datadir/pytrainer/plugins/garmin-hr/conf.xml
%_datadir/pytrainer/plugins/garmin-hr/garminhr.py
%_datadir/pytrainer/plugins/garmin-hr/pytrainer.style
%_datadir/pytrainer/plugins/garmin-hr/translate.xsl
%dir %_datadir/pytrainer/plugins/garmin-tcxv2
%_datadir/pytrainer/plugins/garmin-tcxv2/conf.xml
%_datadir/pytrainer/plugins/garmin-tcxv2/garmin-tcxv2.py
%_datadir/pytrainer/plugins/garmin-tcxv2/translate.xsl
%dir %_datadir/pytrainer/plugins/garmintools
%_datadir/pytrainer/plugins/garmintools/conf.xml
%_datadir/pytrainer/plugins/garmintools/garmintools.py
%_datadir/pytrainer/plugins/garmintools/translate.xsl
%dir %_datadir/pytrainer/plugins/garmintools_full
%_datadir/pytrainer/plugins/garmintools_full/conf.xml
%_datadir/pytrainer/plugins/garmintools_full/garmintools_full.py
%_datadir/pytrainer/plugins/garmintools_full/pytrainer.style
%_datadir/pytrainer/plugins/garmintools_full/translate.xsl
%dir %_datadir/pytrainer/plugins/googleearth
%_datadir/pytrainer/plugins/googleearth/conf.xml
%_datadir/pytrainer/plugins/googleearth/main.py
%_datadir/pytrainer/plugins/googleearth/main.sh
%_datadir/pytrainer/pytrainer.style
%dir %_datadir/pytrainer/schemas
%_datadir/pytrainer/schemas/Cluetrust_gpxdata10.xsd
%_datadir/pytrainer/schemas/GarminTrainingCenterDatabase_v1-gpsbabel.xsd
%_datadir/pytrainer/schemas/GarminTrainingCenterDatabase_v1.xsd
%_datadir/pytrainer/schemas/GarminTrainingCenterDatabase_v2.xsd
%_datadir/pytrainer/schemas/Topografix_gpx11-Nokia.xsd
%_datadir/pytrainer/schemas/Topografix_gpx11.xsd
%_datadir/pytrainer/schemas/atom-author-link.xsd
%_datadir/pytrainer/schemas/garmintools.xsd
%_datadir/pytrainer/schemas/kml20-geodistance.xsd
%_datadir/pytrainer/schemas/ogckml22.xsd
%_datadir/pytrainer/schemas/pytrainer-0.1.xsd
%_datadir/pytrainer/schemas/xAL.xsd

%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus

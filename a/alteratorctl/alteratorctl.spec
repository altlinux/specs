%define _unpackaged_files_terminate_build 1
%define short_name actl

Name: alteratorctl
Version: 0.4.0
Release: alt1

Summary: CLI for alterator-explorer
License: GPL-2.0+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alteratorctl

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake cmake-modules gcc glib2-devel libdbus-glib-devel libgio-devel libpcre2-devel
BuildRequires: libffi-devel zlib-devel libmount-devel libblkid-devel libselinux-devel libtomlc99-devel libgumbo-devel
BuildRequires: libpolkit-devel libjson-glib-devel

Requires: alterator-manager >= 0.1.32
Requires: alterator-module-executor >= 0.1.29
Requires: alterator-backend-packages >= 0.2.19
Requires: alterator-backend-component >= 0.3.6
Requires: alterator-interface-edition >= 0.4.2
Requires: alterator-interface-diag >= 0.1.5
Requires: alterator-backend-systeminfo >= 0.4.3
Requires: alterator-interface-service >= 0.2.1-alt2
Requires: alterator-backend-source >= 0.1.2-alt1
Requires: libtomlc99 polkit libjson-glib

Source0: %name-%version.tar

%filter_from_requires /fish/d
%filter_from_requires /bash/d

%description
A command line tool for using alterator DBus objects.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
ln -s %_bindir/%name %buildroot%_bindir/%short_name

%files
%_bindir/%name
%_bindir/%short_name
%_datadir/alteratorctl/lang/ru/LC_MESSAGES/%name.mo
%_datadir/alteratorctl/scripts/completion_wrapper
%_datadir/alteratorctl/scripts/completion_services
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/bash-completion/completions/%short_name
%_datadir/fish/vendor_completions.d/%short_name.fish

%changelog
* Mon Jun 22 2026 Pavel Khromov <hromovpi@altlinux.org> 0.4.0-alt1
- Added:
  + Module for working with sources.

- Fixed:
  + Fail of `editions list`. (Closes #59536);
  + Helps for components, diag, services, systeminfo, editions modules and packages apt submodule. (Closes #57975);
  + The component module does not allow deleting a component if there is no base section in the edition. (Closes #59514).

* Tue Apr 28 2026 Pavel Khromov <hromovpi@altlinux.org> 0.3.2-alt1
- Fixed:
  + Handling invalid command input in services module;
  + Handling invalid option input when working with services;
  + Handling an attempt to reset a mandatory parameter in service module `configure` command.

* Mon Apr 13 2026 Pavel Khromov <hromovpi@altlinux.org> 0.3.1-alt1
- Fixed:
  + Incorrect behavior of the services module when services are missing (Closes: #58642);
  + Unable to run a separate test via diag module (Closes: #58652).

* Mon Apr 06 2026 Pavel Khromov <hromovpi@altlinux.org> 0.3.0-alt1
- Added:
  + Support for displaying the status of components without categories;
  + Printing components without categories;
  + Supporting of hidden components (added option `--show-hidden`);
  + The ability to call help for various commands without specifying service names;
  + Processing of allowed operations for selected services from their descriptors;
  + Adding mandatory parameter labels to the service module command help;
  + Password roles supporting in services module;
  + Info about current edition in systeminfo module.
- Fixed:
  + Handling an error when attempting to run a diagnostic tool that does not exist on the specified bus;
  + Handling an error when attempting to run a diagnostic tool on a session bus as root;
  + Component installation failing when there are conflicts with manually installed packages;
  + Printing parameters description and comments in `services status` command.
- Changed:
  + More comfortable error message when a service name is incorrect;
  + Get rid of unicode styled tables with services params in services module commands;
  + Remove full parameter dump for showing missed params.

* Wed Feb 18 2026 Pavel Khromov <hromovpi@altlinux.org> 0.2.8-alt1
- Fixed:
  + Components list assertions.
  + Editions list double free.

* Thu Feb 12 2026 Pavel Khromov <hromovpi@altlinux.org> 0.2.7-alt1
- Fixed:
  + Displaying a message about the absence of diagnostic tools in the "diag list".
  + Displaying a message about missing components in the "components list".
- Added:
  + Added support for disabling actions for services for the alterator-entry.
  + Added support for hints for invalid for service values in accordance with the alterator-entry.

* Thu Feb 05 2026 Pavel Khromov <hromovpi@altlinux.org> 0.2.6-alt1
- Fixed:
  + Components module help.
  + Column-based output is used only in interactive mode, where terminal width can be determined.
- Changed:
  + Added check for interactive confirmation availability when installing, removing, or updating packages.
- Added:
  + `--yes` option for package apt install command.

* Fri Jan 30 2026 Pavel Khromov <hromovpi@altlinux.org> 0.2.5-alt1
- Fixed:
  + Services module usage help output.
  + Services module contextual commands usage help output.
  + Fixed a service crash that occurs during the resource conflict checking stage if only one service exists (Closes: #57364).
  + Intercepting attempts to run service diagnostic tests in the absence of service tests.
  + Fixed the missing message about the absence of the selected diagnostic tool.
- Changed:
  + Clarified description of manually installed packages and --allow-remove-manually option (Closes: #57591).

* Mon Jan 19 2026 Pavel Khromov <hromovpi@altlinux.org> 0.2.4-alt1
- Added:
  + Ability to select the "Other components" section in the Components module.
  + Pretty printing of edition license.
- Fixed:
  + Failure to retrieve the edition license (Closes: #57236).
  + Running service diagnostic tests with the `--all` option.
  + Failures when saving reports in the Diagnostics module.
  + Path formatting in the services parameters table.

* Fri Dec 26 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.2.3-alt1
- Changed (thx Andrey Alekseev):
  + Order of parameter validation, parameter table output, and password
    confirmation. Parameters are only validated after the table is displayed.
    Passwords are requested interactively only if all other
    parameters are valid.
- Fixed (thx Pavel Khromov and Andrey Alekseev):
  + Removed parameters from command help that did not match their context.
  + Segmentation faults (play, resource conflict checks, ...).
  + Inaccuracies in output (extra characters, etc.).
  + The play command check would fail if diagnostics were enabled.
  + Incorrect triggering of conflict detection during undeploy.
  + Retrieving the status of the service list.
  + Disabling resource conflict checks within a service during its configuration.
  + Handling of invalid enum values.

* Fri Dec 12 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.2-alt1
- Made params table more pretty.
- Made services module help more detailed.
- Add diagnostic test exit code for "SKIP" state
- Fix parsing of diagnostic tests exit codes.
- Refactor services diagnostic tools running messages.
- Fix filling of default values to enums (thx Andrey Alekseev).
- Support for nested enums in the services module.
- Change deployed status marker (thx Oleg Chagaev).
- Optimize and simplified rendering of service resouces info (thx Oleg Chagaev).

* Wed Nov 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.1-alt1
- Sorting the order of running tests for the selected diagnostic tool.
- Optimizing the launch of diagnostic tests.
- Show parameters description in services play (thx Oleg Chagaev).

* Tue Nov 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.2.0-alt1
- Services module implementation (thx Andrey Alekseev and Oleg Chagaev).
- Fix completions (thx Kozyrev Yuri).
- Fix components (thx Kirill Sharov).

* Tue Sep 16 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.15-alt1
- Fixed printing of components of selected editions.
- Fix of confirmation message for packages apt operations.

* Tue Sep 02 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1.14-alt1
- Fix localization of output of installation/removal of components.
- Fix localization of output of installation/removal/updating of packages by apt.
- Fix sending of wrong locale data to dbus connection.
- Use as instead ay on batch interfaces of components.

* Tue Aug 05 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.13-alt1
- Added:
  + Line breaks for better readability of components install/remove. (by nexi@)
    --force-yes option in components module;
  + Handling warnings in diag run command;
  + Spliting packages apt andd components install/remove output to columns;
  + Handling ^C during apt-get transaction;
    components search command;
  + Pager for components list, packages rpm list/files and packages apt list/search output;
  + Spliting tests output in --verbose mode during diag run.
- Fixed:
  + Handling attempts to remove uninstalled packages and install already installed ones;
  + Names of components removing options;
  + Line breaks in --help option output.
- Changed:
  + Split target components and affected components in install and remove commands;
  + More detailed help in the components module;
  + Increased the version of a required dependency from alterator-interface-edition and
    alterator-backend-systeminfo.

* Sat Jul 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.12-alt1
- Added:
  + Calculating affected components for installing or removing of specified component;
  + Packages filtering in components status, components install or components remove by exclude_arch flags;
  + Show tests display name in diag run by default. (by nexi@)
- Fixed:
  + packages apt list command description; (by nexi@)
  + Settint timeouts for dbus calls with signals.
- Changed:
  + Increased the version of a required dependency from alterator-backend-packages;
  + Moved completions setup logic to completions/CMakeLists.

* Fri Jul 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.11-alt1
- Added:
  + Prevent manual removal of installed packages by default in components remove and packages apt.
- Fixed:
  + Bash-completion working with actl symbolic link to alteratorctl;
  + Send edition path to edition set.

* Tue Jul 01 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.10-alt1
- Fixed typos (thx Elena Mishina).
- Added Bash and Fish completion (thx Kozyrev Yuri).

* Sat May 31 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.9-alt1
- Added:
  + Apt-get output streaming in alteratorctl packages apt install;
  + Apt-get output streaming in alteratorctl packages apt remove;
  + Apt-get output streaming in alteratorctl packages apt reinstall;
  + Apt-get output streaming in alteratorctl packages apt update;
  + Packages apt submodule methods install, remove and reinstall output sorting;
  + Systeminfo module output sorting in description method;
  + Handling dbus errors from connection;
  + Simplify checking of existance of dbus objects;
  + Choose edition sections parameters in components module cmdl;
  + Hide installed status markers in components module;
  + Hide installed edition marker.
- Fixed:
  + alteratorctl manager getsignals fix double free signals names and memory leak;
  + Registration of polkit-agent in tty;
  + Components installed status with architecturally depends packages;
  + Extra printing of specified category in components module;
  + Fixing build requires and creating symbolic link named actl.
- Changed:
  + Renaming --show-display-name option to --enable-display-name in components module. (Closes: #57161)

* Fri Apr 18 2025 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.8-alt1
- fix: fixed package list during install

* Wed Apr 16 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.7-alt1
- Added:
  + --verbose option in editions, diag and components usage help.
- Fixed:
  + Running diagnostic tools from root;
  + Components options translation;
  + Handling set of noexistance edition.
- Changed:
  + Diagnostic tool tests status names;
  + Usage helps alignment.

* Thu Apr 10 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.6-alt1
- Changed:
  + Changed versions in the installation dependencies.
- Fixed:
  + Getting components sections while empty result;
  + Getting components list while DE's is empty;
  + Systeminfo desktop and locales ouptput;
  + Double free in diag list tests;
  + Glib warning in components components while edition doesn't set;
  + Diag test status output;
  + Manager getobjects and getifaces output;
  + Remove packages filtering in components list (this functional moved to batch components backend).

* Tue Apr 01 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.5-alt1
- Added:
  + Systeminfo desktop and locales methods;
  + Filter components packages by languages and desktop environments;
  + Add dependencies from specified required packages;
  + Add LICENSE file.
- Changed:
  + Edit summary and description.
- Fixed:
  + Component packages filtering in components list.

* Thu Mar 27 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.4-alt1
- Added:
  + Textual authentication agent;
  + Add libpolkit-devel to build requires.
- Fixed:
  + Fallback in usage polkit agent;
  + Handling incorrect category name with --category option in components module;
  + Memory leaks in components install/remove;
  + Memory leaks in components list;
  + Memory leaks in components info;
  + Memory leaks in components printing list helper function.

* Wed Mar 26 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.3-alt1
- Added:
  + Component packages filtering by arch option;
  + Include kernel name in package name when kernel_module option is set;
  + Components packages sorting in components status command;
  + New version depending on the version of the alterator-backend-batch-components
    depending on the version.
- Fixed:
  + Components packages installed status markers;
  + Memory leaks;
  + Editions ru. usage help translation;
  + Packages submodules errors handling;
  + Packages rpm list method name;
  + Systeminfo description ignore unknown properties;
  + Components apt update function;
  + Display all components from current edition in default mode;
  + Components installed markers position;
  + Various segfaults and memory leaks;
  + Handling of invalid or missing locales.
- Removed:
  + Warning about the absence of the current edition.

* Tue Mar 18 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.2-alt1
- Added:
  + Sorting result of editions module;
  + Sorting result of diag list method;
  + Sorting result of packages submodules;
  + Components --draft and no-update options;
  + Current edition marker in editions list.
- Removed:
  + Systeminfo license.

* Mon Mar 17 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.1-alt1
- Added:
  + Option to hide the components module legend;
  + Selecting the license text in the systeminfo module depending on the system language;
  + Marker for unknown installed status;
  + Sorting in alteratorctl manager module.
- Security:
  + Changed the user tracking criteria for running commands that require appropriate permissions.
- Fixed:
  + --path-only option usage in components --list;
  + Correct handling of missing edits.

* Thu Mar 13 2025 Pavel Khromov <hromovpi@altlinux.org> 0.1.0-alt1
- Added:
  + Installing status markers legend;
  + Output sorting by names;
  + Systeminfo license.
- Changed:
  + Simple tree output in components module;
  + Option names;
  + Removing unnecessary dependencies.
- Fixed:
  + Printing components while edition isn't valid;
  + Check running via sudo.

* Mon Mar 10 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.11-alt2
- Adding polkit to dependencies

* Fri Mar 07 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.11-alt1
- Added:
  + Editions list and license;
  + Spliting categories and components by editions sections;
  + Adding automatic substitution of current default editions into command arguments of editions module.
- Fixed:
  + Editions info and description methods.

* Thu Mar 06 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.10-alt1
- Adding dependencies on backends of alteratorctl modules

* Tue Feb 25 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.9-alt2
- Adding html parser library libgumbo-devel to build requires

* Mon Feb 17 2025 Pavel Khromov <hromovpi@altlinux.org> 0.0.9-alt1
- Reworking the help calls
- User-friendly interface of the diag module. Make default list tools and list tool tests commands
- Display all information using the default description command in systeminfo module
- Working with components names. Reworking components output

* Fri Dec 13 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.8-alt2
- fix interface validation
- refactor commands

* Tue Dec 10 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.8-alt1
- move to toml

* Thu Nov 07 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.7-alt1
- implement last-update in packages module
- add descriptions to editions in editions module
- fix error messages
- implement sysinfo module
- diag and manager modules can work with objects on system or session buses

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.6-alt1
- change prefix from ru.basealt to org.altlinux
- add systeminfo module

* Wed Oct 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt3
- two ways of getting information about an object are implemented: plain text and keyed parsed content
- fix components and packages modules

* Fri Sep 27 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt2
- fix component module
- implement obtaining information about the object both in text and parsed form

* Mon Sep 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.5-alt1
- implement Alterator Entry parsing
- add diag module

* Thu Aug 22 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.4-alt1
- add common method
- refactor internal client modules to check objects and interfaces
- locale fix
- add translations

* Wed Jul 31 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.3-alt1
- refactor manager module
- implement diag module

* Tue Jul 23 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.2-alt1
- implement manager, packages and components modules

* Sun Jun 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.0.1-alt1
- initial build

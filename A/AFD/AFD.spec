%define oname afd

Name:    AFD
Version: 1.4.20
Release: alt1

Summary: A tool to distribute data
License: GPL-2.0
Group:   Networking/File transfer
Url:     https://github.com/holger24/AFD

Source: %name-%version.tar

BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xaw7)
BuildRequires: libopenmotif-devel

%description
The Automatic File Distributor provides a framework for very flexible,
non-stop, log and debug-able delivery of an arbitrary amount of files to
multiple recipients as expressed in URLs (currently mailing, ftp, ftps,
sftp and http supported with the mailto://user@domain and
ftp://user:password@host URL conventions).

%package -n %oname
Summary: %summary
License: GPL-2.0
Group:   Networking/File transfer

%description -n %oname
AFD has many small programs that can be used to view, control or configure it
via command line. These files are located in the directory $AFD_WORK_DIR/sbin

%package -n afdmon
Summary: A tools to monitor AFD
License: GPL-2.0
Group:   Monitoring

%description -n afdmon
This is a program that monitors the status of other AFD's and the opportunity
to control everything from one interface: mon_ctrl

%prep
%setup

%build
touch AUTHORS NEWS
ln -s Changelog ./ChangeLog
ln -s README.configure README
%autoreconf --include=ac-tools
%configure \
    --enable-systemd=yes \
    --enable-multi_fs_support \
    --enable-sendfile_support \
    --enable-splice_support \
    --enable-afd_mon \
    --with-sysconfigdir=%_sysconfdir/sysconfig
%make_build

%install
install -dv %buildroot%_sysconfdir/{%oname,afdmon}
install -dv %buildroot{%_unitdir,%_sysusersdir,%_tmpfilesdir}
%makeinstall_std
install -pv -m644 scripts/%oname@.service %buildroot%_unitdir
install -pv -m644 scripts/%oname.target %buildroot%_unitdir
install -pv -m644 scripts/afd_environment.conf %buildroot%_sysconfdir/%oname
install -pv -m644 scripts/%oname.sysconfig %buildroot%_sysconfdir/%oname
install -pv -m644 scripts/afdmon@.service %buildroot%_unitdir
install -pv -m644 scripts/afdmon.target %buildroot%_unitdir
install -pv -m644 scripts/afdmon_environment.conf %buildroot%_sysconfdir/afdmon
install -pv -m644 scripts/afdmon.sysconfig %buildroot%_sysconfdir/afdmon

tee >> %buildroot%_sysusersdir/%oname.conf<< EOF
u     afd  -   "Runs AFD"  /home/afd      /sbin/nologin
EOF

tee >> %buildroot%_sysusersdir/afdmon.conf<< EOF
u     afdmon  -   "Runs AFD monitor"  /home/afdmon      /sbin/nologin
EOF

tee >> %buildroot%_tmpfilesdir/%oname.conf<< EOF
d     /home/afd        0700 afd afd - -
EOF

tee >> %buildroot%_tmpfilesdir/afdmon.conf<< EOF
d     /home/afdmon        0700 afdmon afdmon - -
EOF

%pre -n %oname
if [ $1 -eq 1 ]; then
    %sysusers_create_package %oname %_sysusersdir/%oname.conf
    echo "System user %oname created"
    %tmpfiles_create_package %oname %_tmpfilesdir/%oname.conf
    echo "%oname home directory created"
fi

%pre -n afdmon
if [ $1 -eq 1 ]; then
    %sysusers_create_package afdmon %_sysusersdir/afdmon.conf
    echo "System user afdmon created"
    %tmpfiles_create_package afdmon %_tmpfilesdir/afdmon.conf
    echo "afdmon home directory created"
    echo "..."
    echo "For configuring afd_mon you need to create a configuration file"
    echo "$AFD_WORK_DIR/etc/AFD_MON_CONFIG."
fi

%files -n %oname
%_bindir/%oname
%_bindir/afdalarm
%_bindir/afd_auto_config
%_bindir/afdcfg
%_bindir/afdcmd
%_bindir/afd_ctrl
%_bindir/afdd
%_bindir/afdds
%_bindir/afd_environment_wrapper
%_bindir/afd_hex_print
%_bindir/afd_info
%_bindir/afd_load
%_bindir/afd_stat
%_bindir/afd_status
%_bindir/afd_unused_infos
%_bindir/aftp
%_bindir/ahtml_list
%_bindir/alda
%_bindir/aldad
%_bindir/amg
%_bindir/archive_watch
%_bindir/asftp
%_bindir/asmtp
%_bindir/awmo
%_bindir/delete_log
%_bindir/dir_check
%_bindir/dir_ctrl
%_bindir/dir_info
%_bindir/distribution_log
%_bindir/edit_hc
%_bindir/event_log
%_bindir/fd
%_bindir/fra_edit
%_bindir/fra_view
%_bindir/fsa_edit
%_bindir/fsa_view
%_bindir/get_dc_data
%_bindir/get_hostname
%_bindir/get_rr_data
%_bindir/gf_exec
%_bindir/gf_ftp
%_bindir/gf_ftp_trace
%_bindir/gf_http
%_bindir/gf_http_trace
%_bindir/gf_sftp
%_bindir/gf_sftp_trace
%_bindir/grib2wmo
%_bindir/handle_event
%_bindir/init_afd
%_bindir/init_afd_worker
%_bindir/input_log
%_bindir/jid_view
%_bindir/mafd_ctrl
%_bindir/mirror_fra_cfg
%_bindir/mon_unused_infos
%_bindir/mshow_log
%_bindir/output_log
%_bindir/production_log
%_bindir/rafdd_cmd
%_bindir/rafdd_cmd_ssh
%_bindir/raftp
%_bindir/rasftp
%_bindir/receive_log
%_bindir/set_pw
%_bindir/sf_exec
%_bindir/sf_ftp
%_bindir/sf_ftp_trace
%_bindir/sf_http
%_bindir/sf_http_trace
%_bindir/sf_loc
%_bindir/sf_scp
%_bindir/sf_scp_trace
%_bindir/sf_sftp
%_bindir/sf_sftp_trace
%_bindir/sf_smtp
%_bindir/sf_smtp_trace
%_bindir/sf_wmo
%_bindir/sf_wmo_trace
%_bindir/show_bench_stat
%_bindir/show_cmd
%_bindir/show_dlog
%_bindir/show_elog
%_bindir/show_ilog
%_bindir/show_istat
%_bindir/show_log
%_bindir/show_olog
%_bindir/show_plog
%_bindir/show_queue
%_bindir/show_stat
%_bindir/system_log
%_bindir/trans_db_log
%_bindir/transfer_log
%_bindir/udc
%_bindir/uhc
%_bindir/view_dc
%_bindir/xsend_file
%_bindir/xshow_stat
%_sbindir/cache_spy
%_sbindir/convert_fsa
%_sbindir/convert_stat
%_sbindir/current_job_list_spy
%_sbindir/dc_id_spy
%_sbindir/dir_spy
%_sbindir/dup_spy
%_sbindir/file_mask_list_spy
%_sbindir/gen_file
%_sbindir/queue_spy
%_sbindir/rm_job
%_sbindir/set_counter
%_sbindir/set_ls_data
%_sbindir/view_ls_data
%_man1dir/*
%_man5dir/*
%_defaultdocdir/%oname
%config(noreplace) %_sysconfdir/%oname
%_unitdir/%oname@.service
%_unitdir/%oname.target
%_sysusersdir/%oname.conf
%_tmpfilesdir/%oname.conf

%files -n afdmon
%_bindir/afd_mon
%_bindir/afd_mon_status
%_bindir/log_mon
%_bindir/mafd
%_bindir/mafdcmd
%_bindir/mon
%_bindir/mon_ctrl
%_bindir/mon_info
%_bindir/mon_sys_log
%_bindir/monitor_log
%_bindir/msa_view
%_bindir/rmon_ctrl
%_bindir/rmon_ctrl_ssh
%_bindir/topview
%_bindir/view_hosts
%config(noreplace) %_sysconfdir/afdmon
%_unitdir/afdmon@.service
%_unitdir/afdmon.target
%_sysusersdir/afdmon.conf
%_tmpfilesdir/afdmon.conf

%changelog
* Wed Jun 03 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.4.20-alt1
- Initial build for Sisyphus.

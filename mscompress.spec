Summary:	MS compress/expand-compatible (de)compressor
Summary(pl):	(De)kompresor zgodny z MS compress/expand
Name:		mscompress
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://ftp.penguin.cz/pub/users/mhi/mscompress/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%description -l pl
Program kompresuj±cy i dekompresuj±cy zgodny z compress.exe/expand.exe
Microsoftu.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mscompress msexpand $RPM_BUILD_ROOT%{_bindir}
install mscompress.1 msexpand.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO format.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

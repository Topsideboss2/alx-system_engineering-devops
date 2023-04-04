# A puppet file that kills a process 'killmenow'

exec { 'killmenow':
	path => '/usr/bin',
	command => 'pkill killmenow',
	provider => 'shell',
	returns => [0, 1]
}
